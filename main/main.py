from fastapi import FastAPI
from fastapi import Form, UploadFile, File
from pathlib import Path
import os
import logging
from schema import FileUploadedResponse as SchemaFileUploadedResponse
from dotenv import load_dotenv
load_dotenv('.env')

AS=os.getenv('As')
print(AS)
app = FastAPI()
MEDIA_DIR = Path(r"media")
print(MEDIA_DIR)

@app.post('/uploadTrainingDocs/', response_model=SchemaFileUploadedResponse)
async def upload_training_docs(
    doc_name: str = Form(...),
    dir_name: str = Form(...),
    doc: UploadFile = File(...),
):
    # Construct the full directory pathA
    target_dir = MEDIA_DIR / dir_name

    # Create the directory if it does not exist
    target_dir.mkdir(parents=True, exist_ok=True)

    # Handle file upload
    filename, file_extension = os.path.splitext(doc.filename)
    store_path = target_dir / (doc_name + file_extension)
    with open(store_path, "wb") as f:
        contents = await doc.read()
        f.write(contents)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Return the relative path of the uploaded file
    folder_path = str(store_path)
    logging.info(folder_path)
    return {"doc_name": doc_name, "status": 1, "file_path": folder_path}

@app.get("/")  # Add this decorator to link the root endpoint
async def read_root():
    return {"Hello": "Ashish"}
