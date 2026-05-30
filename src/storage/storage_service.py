import os
from pathlib import Path

UPLOAD_DIR = 'uploads'

def save_file(file, filename):
    Path(UPLOAD_DIR).mkdir(exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, 'wb') as buffer:
        buffer.write(file)

    return file_path