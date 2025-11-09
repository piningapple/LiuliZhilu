"""модуль для работы с сервером"""
import uvicorn
from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pinyin import get_seg_and_pin_text
from database_dict import get_translation_with_examples

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def index():
    """главная страница"""
    return FileResponse("static/index.html")

@app.get("/api/translate/")
async def get_translate(ch):
    """получение перевода иероглифа"""
    return get_translation_with_examples(ch)

@app.post("/api/pinyin")
async def get_pinyin(text = Body()):
    """сегментация и получение пиньина"""
    return  get_seg_and_pin_text(text['text'])


if __name__ == "__main__":
    uvicorn.run("server:app", host='127.0.0.1', port=5126, reload=True)
