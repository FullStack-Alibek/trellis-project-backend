import uuid

def generate_3d(image_path: str):
    filename = f"{uuid.uuid4()}.glb"

    with open(f"uploads/{filename}", "w") as f:
        f.write("fake glb model")

    return filename