from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI()

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    with open("received_audio.wav", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Audio recibido correctamente"}
