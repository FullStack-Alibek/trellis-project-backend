from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File
from src.routers.routers_generate import router as generate_router
from src.routers.job import router as job_router
import os

app = FastAPI()
app.include_router(job_router)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"health": "ok"}

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "filename": file.filename,
        "saved_to": file_path
    }

app.include_router(generate_router)