import os, shutil, time, logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pypdf import PdfReader
from docling.document_converter import DocumentConverter

# --- PATH SETUP ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# IMPORTANT: Point this to your existing hf_cache folder
EXISTING_CACHE = "/Users/sureshsonwane/Desktop/vscprojects/stage_1/hf_cache"
os.environ["HF_HOME"] = EXISTING_CACHE

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("--- STARTUP: Initializing Docling (Defaults) ---")
    # No configuration passed, letting Docling handle everything automatically
    app.state.converter = DocumentConverter()
    yield
    if hasattr(app.state, 'converter'): 
        del app.state.converter

app = FastAPI(lifespan=lifespan)
os.makedirs(os.path.join(BASE_DIR, "uploads"), exist_ok=True)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.post("/compare")
async def compare(request: Request, file: UploadFile = File(...)):
    file_path = os.path.join(BASE_DIR, "uploads", file.filename)
    with open(file_path, "wb") as buffer: 
        shutil.copyfileobj(file.file, buffer)
    
    # 1. Traditional Extraction (pypdf)
    t_start = time.time()
    reader = PdfReader(file_path)
    trad_out = "\n".join([f"--- PAGE {i+1} ---\n{p.extract_text()}" for i, p in enumerate(reader.pages)])
    t_time = f"{time.time() - t_start:.2f}s"
    
    # 2. Docling Extraction (Default AI Logic)
    d_start = time.time()
    result = request.app.state.converter.convert(file_path)
    doc_out = result.document.export_to_markdown()
    d_time = f"{time.time() - d_start:.2f}s"
    
    return {
        "traditional": trad_out,
        "docling": doc_out,
        "metrics": {"trad_time": t_time, "docling_time": d_time}
    }

@app.get("/", response_class=HTMLResponse)
async def index():
    with open(os.path.join(BASE_DIR, "static/index.html")) as f: 
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)