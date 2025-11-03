from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from database_dict import get_translation_with_examples

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/api/translate/")
async def get_translate(ch):
    return get_translation_with_examples(ch)

if __name__ == "__main__":
    uvicorn.run("server:app", host='127.0.0.1', port=8000, reload=True)
