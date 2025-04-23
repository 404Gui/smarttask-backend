# SmartTask 🧠

Projeto pessoal de um sistema de gerenciamento de tarefas. A ideia é ter um to-do list mais completo, com backend em **FastAPI + PostgreSQL**, e frontend em **React com TypeScript**.

---

## Tecnologias (backend)

- FastAPI
- PostgreSQL (via Docker)
- SQLAlchemy
- Pydantic
- Python 3.11+
- Docker (somente pro banco)

---

## O que já tá funcionando

- Estrutura inicial da API
- CRUD completo de tarefas:
  - `GET` todas ou uma tarefa específica
  - `POST` nova tarefa
  - `PUT` pra atualizar
  - `DELETE` pra remover
- Integração com PostgreSQL
- Schemas e validações com Pydantic

---

## Próximos passos

- [ ] Autenticação com JWT
- [ ] Relacionar usuários com tarefas
- [ ] Criar testes
- [ ] Subir pra produção (Railway talvez)
- [ ] Iniciar o frontend com Next.js

---

## Como rodar o backend

1. Clonar o projeto e entrar na pasta:

```bash
git clone https://github.com/404Gui/smarttask-backend
cd smarttask-backend
