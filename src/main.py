from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import engine
from src.auth.router import router as auth_router
import src.models as user_models

user_models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "hello to the root"}