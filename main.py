from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from collections import Counter

app = FastAPI()

@app.post("/analyze/")
async def analyze_text(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    words = text.split()
    lines = text.splitlines()
    word_count = len(words)
    line_count = len(lines)
    avg_word_length = round(sum(len(word) for word in words) / word_count, 2) if word_count else 0

    freq = Counter(words)
    most_common = freq.most_common(1)[0] if freq else ("None", 0)

    return JSONResponse({
        "word_count": word_count,
        "line_count": line_count,
        "average_word_length": avg_word_length,
        "most_frequent_word": most_common[0],
        "frequency": most_common[1]
    })