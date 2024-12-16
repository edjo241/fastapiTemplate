import os
from fastapi import HTTPException, UploadFile

def save_file(file: UploadFile, upload_dir:str):
    try:
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        file_path = os.path.join(upload_dir, file.filename) 
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        return file_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))