from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import auth, journal, entries
import os

app = FastAPI()

# CORS (allow frontend dev server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static file server for uploaded files
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(journal.router, prefix="/journal", tags=["journal"])
app.include_router(entries.router, prefix="/entries", tags=["entries"])

@app.get("/")
def root():
    return {"message": "StashBrain backend is running."}
