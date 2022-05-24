# main.py
from fastapi import FastAPI, File, UploadFile
from dectertor import run_detect_img

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hola"}

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        await file.close()
    
    detected = run_detect_img(file.filename)
        
    return {"Detect": detected}