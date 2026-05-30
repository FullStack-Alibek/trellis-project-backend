from fastapi import APIRouter
from src.schemas.schemas_generate import GenerateRequest
from src.services.job_service import create_job
from fastapi.responses import FileResponse


router = APIRouter()

@router.post("/generate-3d")
async def generate_3d(data: GenerateRequest):
    
    job = create_job(data.image_url)
    
    return {
        "job_id": job["job_id"],
        "status": job["status"],
        "image_url": data.image_url,
    }
    
@router.get("/download/{filename}")
def download_model(filename: str):
    return FileResponse(
        path=f"uploads/{filename}",
        filename=filename
    )