import shutil
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfile/", tags=['UPLOAD'])
async def create_upload_file(file: UploadFile = File(...)):
    file_path = f'./{file.filename}'
    try:
        with open(file_path, 'wb+') as file_obj:
            file_obj.write(file.file.read())
        message = "Upload realizado com sucesso!"
    except Exception as e:
        message = "Erro ao fazer upload do arquvio!"

    return {"message": message}
