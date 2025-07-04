# 🎯 Quiz API - FastAPI + PostgreSQL (Neon)

API REST para criação e gerenciamento de quizzes, com autenticação JWT, controle de permissões por papel (admin/usuário) e persistência em banco de dados PostgreSQL (Neon.tech).

---

## 🚀 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Neon.tech (cloud PostgreSQL)](https://neon.tech/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [Passlib (bcrypt)](https://passlib.readthedocs.io/)
- [JWT - PyJWT](https://pyjwt.readthedocs.io/)


## 📂 Estrutura do Projeto

```bash
api-fastapi/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── auth/
│   │   ├── auth.py
│   │   └── dependencies.py
│   ├── routes/
│   │   ├── usuarios.py
│   │   ├── quizzes.py
│   │   ├── perguntas.py
│   │   └── resultados.py
│   └── schemas.py
├── .env
├── requirements.txt
└── README.md
```

---


---

## ⚙️ Configuração

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/quiz-api-fastapi.git
cd quiz-api-fastapi

2. Crie e ative um ambiente virtual
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Configure o arquivo .env
Crie um arquivo .env na raiz com as seguintes variáveis:

env
Copiar
Editar
DATABASE_URL=postgresql://usuario:senha@ep-host.aws.neon.tech/nome_do_banco
SECRET_KEY=sua_chave_jwt
💡 O DATABASE_URL é fornecido pelo painel do Neon.

▶️ Rodando o servidor local
bash
Copiar
Editar
uvicorn app.main:app --reload
Acesse: http://localhost:8000/docs

🔐 Funcionalidades de Autenticação
Registro de usuário (com role usuario por padrão)

Login com JWT

Middleware que protege rotas autenticadas

Controle de acesso por role (admin pode criar quizzes, por exemplo)

📚 Endpoints principais
Método	Rota	Descrição
POST	/usuarios/register	Criar um novo usuário
POST	/usuarios/login	Login e geração de token JWT
POST	/quizzes/	Criar quiz (admin)
GET	/quizzes/{id}/perguntas	Ver perguntas de um quiz
POST	/perguntas/	Criar pergunta (admin)
POST	/resultados/	Salvar resultado
GET	/usuarios/{id}/resultados	Ver resultados do usuário
POST	/usuarios/esqueci-senha	Geração e envio de nova senha por e-mail

🌐 CORS liberado
As requisições de qualquer origem estão liberadas via middleware CORS:

python
Copiar
Editar
allow_origins=["*"]
📝 Licença
Este projeto está licenciado sob a MIT License.
