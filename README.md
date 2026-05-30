# Trellis Project Backend

FastAPI backend for image-to-3D model generation.

## Features

* Upload image
* Generate 3D model
* Download generated `.glb` file
* Docker support

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Run with Docker

```bash
docker compose up --build
```

## API Endpoints

* `POST /upload-image` — Upload image
* `POST /generate-3d` — Generate 3D model
* `GET /job/{job_id}` — Check job status
* `GET /download/{filename}` — Download generated model

## Tech Stack

* FastAPI
* Docker
* Python 3.13
* Uvicorn
