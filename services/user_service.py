from fastapi import  HTTPException, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from models.user_dto import CreateUserDTO, UserDTO
from passlib.context import CryptContext


from schemas.user_schema import UserSchema

#region password utilities

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

#endregion

#region user db operations
async def create_user(user: CreateUserDTO, db: Session = Depends(get_db())) -> UserDTO:
    hashed_password = hash_password(user.password)
    db_user = UserSchema(username=user.username, email=user.email, role="user", hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not created")
    return UserDTO(id=db_user.id, username=db_user.username, email=db_user.email, role=db_user.role, created_at = db_user.created_at, updated_at = db_user.updated_at)


async def get_users(db: Session = Depends(get_db())) -> list[UserDTO]:
    db_users = db.query(UserSchema).all()
    return [UserDTO(id=db_user.id, username=db_user.username, email=db_user.email, role=db_user.role, created_at = db_user.created_at, updated_at = db_user.updated_at) for db_user in db_users]

async def edit_user(user: UserDTO, db: Session = Depends(get_db())) -> UserDTO:
    db_user = db.query(UserSchema).filter(UserSchema.id == user.id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.username = user.username
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return UserDTO(id=db_user.id, username= db_user.username, email=db_user.email, role=db_user.role, created_at = db_user.created_at, updated_at = db_user.updated_at)

async def detail_user(user_id: int, db: Session = Depends(get_db())) -> UserDTO:
    db_user = db.query(UserSchema).filter(UserSchema.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserDTO(id=db_user.id, username=db_user.username, email=db_user.email, role=db_user.role, created_at = db_user.created_at, updated_at = db_user.updated_at)

async def delete_user(user_id: int, db: Session = Depends(get_db())) -> UserDTO:
    db_user = db.query(UserSchema).filter(UserSchema.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return UserDTO(id=db_user.id, username=db_user.username, email=db_user.email, role=db_user.role, created_at = db_user.created_at, updated_at = db_user.updated_at)
#endregion

