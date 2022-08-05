import sys
sys.path.append("..")
from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    APIRouter
)
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError


SECRET_KEY = "qwacckhnbdff55ky674"
ALGOTITHM = 'HS256'


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
    phone_number: Optional[str]


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={401: {"user": "Not authorized"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password, hashed_password):
    print(f"ffffffffff: {plain_password}, {hashed_password}")
    print(f"ddddddddddddddddd: {bcrypt_context.verify(plain_password, hashed_password)}")
    return bcrypt_context.verify(plain_password, hashed_password)


def authenicate_user(username: str, password: str, db):
    user = db.query(models.Users).filter(models.Users.username == username).first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, expire_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGOTITHM)

async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGOTITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None and user_id is None:
            raise get_user_exception()
        return {"username": username, "id": user_id}
    except JWTError:
        raise get_user_exception()

@router.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = models.Users()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name
    create_user_model.phone_number = create_user.phone_number

    hash_password = get_password_hash(create_user.password)

    create_user_model.hashed_password = hash_password
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenicate_user(form_data.username, form_data.password, db)

    if not user:
        raise token_exception()
    token_expire = timedelta(minutes=20)
    token = create_access_token(user.username, user.id, expire_delta=token_expire)
    return {"token": token}


@router.get("/users")
async def create_new_user( db: Session = Depends(get_db)):
    return db.query(models.Users)\
        .all()
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJxd2VyIiwiaWQiOjEsImV4cCI6MTY1MzE0NzM1M30.rcvk4PyifiMaMTqQMF1Ku42XfOml9KZcoHegEpXOVU4

def get_user_exception():
    creadentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate creadentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return creadentials_exception


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or user_id",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return token_exception_response
