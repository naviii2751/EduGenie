from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from backend.ai.model import ask_gemini

app = FastAPI(title="EduGenie")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Question(BaseModel):
    question: str


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/ask")
def ask(question: Question):
    answer = ask_gemini(question.question)
    return {"answer": answer}