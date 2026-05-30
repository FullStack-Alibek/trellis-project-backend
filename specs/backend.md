# Backend Architecture

## Overview

The backend is built with FastAPI and provides APIs for image upload, 3D model generation, job tracking, and file download.

## API Endpoints

### GET /

Returns API status.

### GET /health

Health check endpoint.

### POST /upload-image

Uploads an image and stores it in the uploads directory.

Response:

```json
{
  "filename": "image.png"
}
```

### POST /generate-3d

Starts 3D model generation.

Response:

```json
{
  "job_id": "uuid",
  "status": "processing"
}
```

### GET /job/{job_id}

Returns current job status.

Response:

```json
{
  "job_id": "uuid",
  "status": "completed"
}
```

### GET /download/{filename}

Downloads generated GLB model.

---

## Processing Flow

1. User uploads image.
2. Backend saves image.
3. Backend starts 3D generation task.
4. Job status becomes processing.
5. Generated .glb file is stored.
6. Job status becomes completed.
7. User downloads generated file.

---

## Storage

### uploads/

Stores uploaded images.

### generated/

Stores generated GLB files.

---

## Docker

Run application:

```bash
docker compose up --build
```

Application URL:

```text
http://localhost:8000
```