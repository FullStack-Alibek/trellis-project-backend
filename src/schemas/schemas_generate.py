from pydantic import BaseModel

class GenerateRequest(BaseModel):
    image_url: str
    prompt: str | None = None