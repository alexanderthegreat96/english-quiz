from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from question_provider import *

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnswerSubmission(BaseModel):
    question_index: int
    selected_index: int

@app.get("/questions")
def get_questions():
    sanitized = []
    for q in questions_db:
        sanitized.append({
            "question": q["question"].replace("{blank}", "_______"),
            "variants": q["variants"]
        })
    return sanitized

@app.post("/validate")
def validate_answer(submission: AnswerSubmission):
    if submission.question_index >= len(questions_db):
        raise HTTPException(status_code=404, detail="Question not found")
    
    correct_idx = questions_db[submission.question_index]["answer"]
    is_correct = submission.selected_index == correct_idx
    
    return {
        "is_correct": is_correct,
        "correct_word": questions_db[submission.question_index]["variants"][correct_idx]
    }