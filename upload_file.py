from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files")
async def create_file(file: bytes = File()):
    with open("./test_files.wav", 'wb') as f:
        f.write(file)
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    with open("./test.wav", 'wb') as f:
        f.write(contents)
    return {"filename": file.filename}
