import sys
sys.path.append("..")
from fastapi import APIRouter, Depends

from database import SessionLocal
from sqlalchemy.orm import Session

import models

router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/")
async def get_company_name():
    return {"company_name": "Example Company, LLC"}

@router.get("/employees")
async def number_of_employees(db: Session = Depends(get_db)):
    return db.query(models.Users.id).all()


