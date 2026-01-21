# 🚀 Document Parsing POC — Stage 1

Welcome to the shiny playground where old-school PDF text extraction meets layout-aware, AI-driven parsing. This repository demonstrates how a layout-first parser (Docling) can drastically improve fidelity for Retrieval-Augmented Generation (RAG) pipelines.

Think of this as: pypdf vs. Docling — a friendly duel to see who understands a document better.

---

## Highlights
- FastAPI backend + tiny frontend UI for instant comparisons.
- Side-by-side outputs: traditional (pypdf) vs Docling (AI/layout-aware).
- Built-in test PDF generators to stress layout, tables, and edge cases.
- Local HF model cache support for offline dev / reproducible runs.

---

## What's in the repo
- [poc/main.py](poc/main.py) — FastAPI service with Docling lifecycle
- [poc/static/index.html](poc/static/index.html) — minimal interactive frontend
- [traditional_pdf_parsing.py](traditional_pdf_parsing.py) — baseline pypdf extraction examples
- [docling_pdf_parsing.py](docling_pdf_parsing.py) — Docling demo usage
- [extreme_pdf_generator.py](extreme_pdf_generator.py), complex_pdf_generator.py — synthetic PDFs to break parsers
- [report_stage_1.md](report_stage_1.md), [report2_stage_1.md](report2_stage_1.md) — quick findings & notes
- [hf_cache/](hf_cache) — (local) Hugging Face cache for models

---

## Quickstart (macOS)
Prereqs:
- Python 3.9+
- pip packages: fastapi, uvicorn, pypdf, docling, reportlab

Install:
```sh
pip install fastapi uvicorn pypdf docling reportlab
```

Run (dev):
```sh
# point to local HF cache (optional but recommended)
mkdir hf_cache
export HF_HOME= ./hf_cache

# from repo root
python poc/main.py

# or:
cd poc
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open: http://localhost:8000 — upload a PDF, hit Parse, and watch the two outputs tango.

---

## Developer tips
- Docling is initialized once on app startup via FastAPI lifespan — hot-reload will recreate it.
- Generate test PDFs:
```sh
python extreme_pdf_generator.py
python complex_pdf_generator.py
```
- Switch HF cache quickly:
```sh
export HF_HOME=/path/to/other/cache && pkill -f uvicorn && uvicorn poc.main:app --reload
```

---

## Known quirks
- Docling may attempt to download models if HF cache isn't populated. 
- Very large PDFs may increase memory/time — watch the terminal logs.

---

## Examples / Expected flow
1. Upload PDF
2. Backend runs:
   - pypdf extraction (plain text, page-wise)
   - Docling extraction (structure, tables, metadata → Markdown)
3. UI shows both results and timing metrics for quick comparison


---

## License & Attribution
This proof-of-concept is meant for experimentation and learning. Check individual third-party model licenses inside `hf_cache/` before production use.

---

Made with curiosity and a fondness for parsing edge-cases. Enjoy!