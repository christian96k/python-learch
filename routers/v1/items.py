from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from manager.item_manager import ItemsManager
from models.item_dto import ItemDTO, ItemCreateDTO
from tags.tags import TagsEnum

router = APIRouter(prefix="/items", tags=[TagsEnum.ITEMS])

@router.post("", response_model=ItemDTO)
async def create_item_endpoint(item: ItemCreateDTO, db: Session = Depends(get_db)):
    manager = ItemsManager(db)
    return await manager.manage_create_item(item)

@router.get("", response_model=list[ItemDTO])
async def list_items_endpoint(db: Session = Depends(get_db)):
    manager = ItemsManager(db)
    return await manager.manage_list_items()

@router.get("/{item_id}", response_model=ItemDTO)
async def get_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    manager = ItemsManager(db)
    return await manager.manage_get_item(item_id)

@router.put("", response_model=ItemDTO)
async def edit_item_endpoint(item: ItemDTO, db: Session = Depends(get_db)):
    manager = ItemsManager(db)
    return await manager.manage_edit_item(item)

@router.delete("/{item_id}")
async def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    manager = ItemsManager(db)
    return await manager.manage_delete_item(item_id)