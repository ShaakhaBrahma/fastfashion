import uvicorn
from fastapi import FastAPI, File, Form, UploadFile
from keras.models import model_from_json
import os
import tempfile
import numpy as np
from PIL import Image
from io import BytesIO
import constants
from col import get_color_name




app = FastAPI()
model = None


@app.get('/')
def check_health():
    return {"message": "Fashion server is up"}


'''@app.post("/files/")
async def create_file(file: bytes = File(...)):
    stream = BytesIO(file)
    color_image = Image.open(stream)
    image = np.array(color_image.convert("L").resize((28, 28)))
    pred_fit_image = image.reshape((1, 28, 28, 1))
    global model
    color_array = (color_image.getcolors(maxcolors=999999))
    intended_color_count = color_array[0][0]
    intended_color = color_array[0][1]
    for _ in color_array:
        if _[0] > intended_color_count:
            intended_color_count = _[0]
            intended_color = _[1]
    return {"file_size": len(file),"color":intended_color, "color_count":intended_color_count}'''
@app.post("/files/")
async def create_file(
    file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    
    return {"filename": file.filename}

@app.post('/predict')
async def predict(file: UploadFile = File(...), user_id: str = Form(...)):
    #stream = BytesIO(file)

    color_image = Image.open(file.file)
    path = "Images/"+user_id+"/"+file.filename
    color_image.save(path, "JPEG")
    image = np.array(color_image.convert("L").resize((28, 28)))
    pred_fit_image = image.reshape((1, 28, 28, 1))
    global model
    probs = model.predict(pred_fit_image)
    color_image = Image.open(file.file)
    height, width = color_image.size
    srow=int(height*.33)
    scol=int(width*.33)
    erow=int(height*.66)
    ecol=int(width*.66)
    crop = color_image.crop((srow, scol, erow, ecol))
    color_array = (crop.getcolors(maxcolors=999999))
    intended_color_count = color_array[0][0]
    intended_color = color_array[0][1]
    for _ in color_array:
        if _[0] > intended_color_count:
            intended_color_count = _[0]
            intended_color = _[1]
    #color_name=intended_color
    color_name = get_color_name(intended_color)
    if color_name==None:
        color_name = intended_color
    label = constants.labelNames[np.argmax(probs)]
    return {"label": label, "color": color_name, "path": path}
'''"rgb": intended_color, "color_count": intended_color_count'''


def run_server(model_path, host, port):
    json_file = open('fmnist.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    global model
    model = model_from_json(loaded_model_json)
    model.load_weights("./fmnist.h5")
    uvicorn.run(app, host=host, port=port)


if __name__ == '__main__':
    run_server("./fmnist.h5", "127.0.0.1", 8000)
