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


class Topic(BaseModel):
    topic: str


class TextInput(BaseModel):
    text: str


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


@app.post("/explain")
def explain(topic: Topic):
    prompt = f"Explain the following topic in a simple and easy-to-understand way for a student: {topic.topic}"
    answer = ask_gemini(prompt)
    return {"answer": answer}


@app.post("/summarize")
def summarize(data: TextInput):
    prompt = f"Summarize the following text clearly and briefly: {data.text}"
    answer = ask_gemini(prompt)
    return {"summary": answer}


@app.post("/quiz")
def quiz(topic: Topic):
    prompt = f"""
Create a short quiz about {topic.topic}.

Generate 3 multiple-choice questions.
Each question must have 4 options.
Clearly identify the correct answer.

Format:
Q1. Question
A) Option
B) Option
C) Option
D) Option
Correct Answer: X
"""
    answer = ask_gemini(prompt)
    return {"quiz": answer}


@app.post("/learning-path")
def learning_path(topic: Topic):
    prompt = f"""
Create a structured learning path for {topic.topic}.

Include:
1. Beginner level
2. Intermediate level
3. Advanced level
4. Important topics to learn at each level
5. Suggested timeline
6. Practice suggestions

Keep it clear and useful for a student.
"""
    answer = ask_gemini(prompt)
    return {"learning_path": answer}