from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze/")
async def analyze_text(file: UploadFile = File(...)):
    contents = await file.read()
    text = contents.decode("utf-8")

    word_count = len(text.split())
    char_count = len(text)
    line_count = text.count("\n") + 1

    return {
        "filename": file.filename,
        "word_count": word_count,
        "char_count": char_count,
        "line_count": line_count
    }