import uuid 
import threading
import time
from src.storage.trellis_service import generate_3d

jobs = {}

def process_job(job_id):
    jobs[job_id]["status"] = "processing"
    
    image_path = jobs[job_id]['image_path']

    result = generate_3d(image_path)

    jobs[job_id]['status'] = 'completed'
    jobs[job_id]['download_url'] = f"/download/{result}"


def create_job(image_path: str):
    job_id = str(uuid.uuid4())
    
    jobs[job_id] = {
        "job_id": job_id,
        'image_path': image_path,
        "status": "queued"
    }
    
    threading.Thread(
        target=process_job,
        args=(job_id,),
        daemon=True
    ).start()
    
    return jobs[job_id]

def get_job(job_id: str):
    return jobs.get(job_id)