## FastAPI Structure
https://github.com/zhanymkanov/fastapi-best-practices

### 1. Fastapi-Base-Project

├── src
│   ├── auth
|   |   ├── config.py   # local configs
│   │   ├── constants.py
│   │   ├── dependencies.py
│   │   ├── exceptions.py
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── service.py
│   │   └── utils.py
│   ├── email
|   |   ├── config.py
│   │   ├── email.py
│   │   ├── schemas.py  # pydantic models
│   │   └── utils.py
│   └── user
|   |   ├── config.py 
│   │   ├── exceptions.py
│   |   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── service.py
│   │   └── utils.py
│   ├── config.py  # global configs
│   ├── database.py  # db connection related stuff
│   ├── exceptions.py  # global exceptions
│   ├── models.py  # global models
│   └── main.py
├── requirements
│   ├── base.txt
│   └── dev.txt
├── .env
├── .gitignore
└── alembic.ini