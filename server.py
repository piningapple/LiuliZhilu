from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from database_dict import get_translation_with_examples
from pinyin import getSegAndPinText

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/api/translate/")
async def get_translate(ch):
    return get_translation_with_examples(ch)

@app.post("/api/pinyin")
async def get_pinyin(text = Body()):
    return  getSegAndPinText(text['text'])
    

if __name__ == "__main__":
   uvicorn.run("server:app", host='0.0.0.0', port=5126, reload=True)
