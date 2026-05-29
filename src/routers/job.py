from fastapi import APIRouter
from src.services.job_service import get_job

router = APIRouter()

@router.get("/job/{job_id}")
async def job_status(job_id: str):
    job = get_job(job_id)
    
    if not job: 
        return {"error": "job not found"}
    
    return job