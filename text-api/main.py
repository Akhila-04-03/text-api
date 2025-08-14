from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    words = text.split()
    word_count = len(words)
    line_count = text.count("\n") + 1
    avg_length = round(sum(len(w) for w in words) / word_count, 2) if word_count else 0
    most_common = max(set(words), key=words.count) if words else ""
    frequency = words.count(most_common) if words else 0

    return {
        "word_count": word_count,
        "line_count": line_count,
        "average_word_length": avg_length,
        "most_frequent_word": most_common,
        "frequency": frequency
    }