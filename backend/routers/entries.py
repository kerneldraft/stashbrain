from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from database import get_db
from models import Entry, User
from routers.journal import get_current_user

router = APIRouter()

class EntryModel(BaseModel):
    title: str
    content: Optional[str] = ""
    type: str  # 'link', 'idea', 'file', 'task'
    tags: Optional[str] = ""
    source: Optional[str] = ""
    status: Optional[str] = "inbox"

@router.post("/")
def create_entry(entry: EntryModel, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_entry = Entry(
        user_id=current_user.id,
        title=entry.title,
        content=entry.content,
        type=entry.type,
        tags=entry.tags,
        source=entry.source,
        status=entry.status,
        created_at=datetime.utcnow()
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.get("/", response_model=List[EntryModel])
def get_entries(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    entries = db.query(Entry).filter(Entry.user_id == current_user.id).order_by(Entry.created_at.desc()).all()
    return entries
