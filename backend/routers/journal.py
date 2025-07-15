from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, datetime
from pydantic import BaseModel

from database import get_db
from models import Journal, User
from routers.auth import jwt, SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt as jose_jwt

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class JournalEntryModel(BaseModel):
    content: str

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jose_jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication")
        user = db.query(User).get(int(user_id))
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

@router.get("/")
def get_today_journal(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    today = date.today()
    journal = (
        db.query(Journal)
        .filter(Journal.user_id == current_user.id, Journal.date == today)
        .first()
    )
    if journal:
        return {"content": journal.content}
    return {"content": ""}

@router.post("/")
def save_journal(entry: JournalEntryModel, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    today = date.today()
    journal = (
        db.query(Journal)
        .filter(Journal.user_id == current_user.id, Journal.date == today)
        .first()
    )
    if journal:
        journal.content = entry.content
        journal.updated_at = datetime.utcnow()
    else:
        journal = Journal(
            user_id=current_user.id,
            date=today,
            content=entry.content
        )
        db.add(journal)
    db.commit()
    return {"message": "Saved"}
