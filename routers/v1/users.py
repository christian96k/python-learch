# Nel tuo user_router.py

from fastapi import APIRouter, HTTPException, Depends
from models.user_dto import UserDTO, CreateUserDTO
from sqlalchemy.orm import Session
from database.dependencies import get_db
from manager.user_manager import UserManager
from tags.tags import TagsEnum

router = APIRouter(prefix="/users", tags=[TagsEnum.USERS])

user_manager = UserManager()

@router.post("", response_model=UserDTO)
async def create_user(user: CreateUserDTO, db: Session = Depends(get_db)):
    try:
        # Passa db come parametro
        return await user_manager.manage_create_user(user, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=f"Error in user creation: {str(e)}")

@router.get("", response_model=list[UserDTO])
async def get_users(db: Session = Depends(get_db)):
    try:
        # Passa db come parametro
        return await user_manager.manage_get_users(db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=f"Error in fetching users: {str(e)}")

@router.put("/{user_id}", response_model=UserDTO)
async def edit_user(user_id: int, user: UserDTO, db: Session = Depends(get_db)):
    try:
        # Passa db come parametro
        return await user_manager.manage_edit_user(user, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=f"Error in updating user: {str(e)}")

@router.get("/{user_id}", response_model=UserDTO)
async def get_user_details(user_id: int, db: Session = Depends(get_db)):
    try:
        # Passa db come parametro
        return await user_manager.manage_detail_user(user_id, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=f"User not found: {str(e)}")

@router.delete("/{user_id}", response_model=UserDTO)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return await user_manager.manage_delete_user(user_id, db)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=f"Error in deleting user: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
