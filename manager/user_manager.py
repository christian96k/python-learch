from services.user_service import create_user, get_users, edit_user, detail_user, delete_user
from models.user_dto import CreateUserDTO, UserDTO
from sqlalchemy.orm import Session
from fastapi import HTTPException

class UserManager:
    def __init__(self):
        pass

    async def manage_create_user(self, user: CreateUserDTO, db: Session) -> UserDTO:
        try:
            user_data = await create_user(user, db)
            if not user_data:
                raise HTTPException(status_code=400, detail="User creation failed but no exception raised.")
            return user_data
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=f"Error in user creation: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


    async def manage_get_users(self, db: Session) -> list[UserDTO]:
        try:
            users = await get_users(db)
            return users
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error in retrieving users")

    async def manage_edit_user(self, user: UserDTO, db: Session) -> UserDTO:
        try:
            updated_user = await edit_user(user, db)
            return updated_user
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=f"Error in updating user: {str(e)}")

    async def manage_detail_user(self, user_id: int, db: Session) -> UserDTO:
        try:
            user_details = await detail_user(user_id, db)
            return user_details
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=f"Error in fetching user details: {str(e)}")


    async  def manage_delete_user(self, user_id: int, db: Session) -> UserDTO:
        try:
            user = await delete_user(user_id, db)
            return user
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=f"Error in deleting user: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")