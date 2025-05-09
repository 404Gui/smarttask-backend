from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
import httpx
import os
from app.auth import create_access_token
from app.models import User
from app.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/auth/google/callback"


@router.get("/auth/google/login")
def login_google():
    google_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        f"?client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&response_type=code"
        "&scope=openid%20email%20profile"
    )
    return RedirectResponse(google_url)


@router.get("/auth/google/callback")
async def google_callback(code: str, db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        token_resp = await client.post("https://oauth2.googleapis.com/token", data={
            "code": code,
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
            "grant_type": "authorization_code"
        })
        token_data = token_resp.json()
        access_token = token_data.get("access_token")

        user_info_resp = await client.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        user_info = user_info_resp.json()
        email = user_info.get("email")

        # Verifica/cria usuário no banco
        user = db.query(User).filter_by(email=email).first()
        if not user:
            user = User(
                email=email,
                username=user_info["name"],
                hashed_password="google_oauth"
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        # Cria token usando username
        jwt_token = create_access_token({"sub": user.username})

        # Redireciona para o frontend com o token
        return RedirectResponse(f"http://localhost:3000/login?token={jwt_token}")

