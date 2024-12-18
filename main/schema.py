from pydantic import BaseModel


class FileUploadedResponse(BaseModel):
    doc_name:str
    status:int
    file_path:str

    class Config:
        orm_mode = True