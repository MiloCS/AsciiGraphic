import os
import shutil
import tempfile
from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
import numpy as np

from tiling.load_images import load_images, load_base_image
from tiling.create_tiled_image import construct_tiling
from ascii.image import image_to_ascii_string

app = FastAPI()
os.makedirs("static/results", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    return FileResponse("static/index.html")

@app.post("/api/ascii")
async def generate_ascii(target_image: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        content = await target_image.read()
        tmp.write(content)
        tmp_path = tmp.name
    
    try:
        ascii_str = image_to_ascii_string(tmp_path)
    finally:
        os.remove(tmp_path)
        
    return {"ascii": ascii_str}

@app.post("/api/tile")
async def generate_tiling(target_image: UploadFile = File(...), batch_images: list[UploadFile] = File(...)):
    temp_dir = tempfile.mkdtemp()
    
    try:
        batch_dir = os.path.join(temp_dir, "batch")
        os.makedirs(batch_dir)
        
        count = 0
        for img in batch_images:
            if count >= 30:
                break
            if img.filename:
                file_path = os.path.join(batch_dir, f"batch_{count}.jpg")
                with open(file_path, "wb") as f:
                    f.write(await img.read())
                count += 1
                
        target_path = os.path.join(temp_dir, "target.jpg")
        with open(target_path, "wb") as f:
            f.write(await target_image.read())
            
        i = load_images(batch_dir)
        b = load_base_image(target_path)
        c = construct_tiling(i, b)
        
        result_img = Image.fromarray(np.uint8(c)).convert('RGB')
        result_filename = f"tiled_{os.urandom(4).hex()}.jpg"
        result_path = os.path.join("static/results", result_filename)
        result_img.save(result_path)
        
        return {"result_url": f"/static/results/{result_filename}"}
        
    finally:
        shutil.rmtree(temp_dir)
