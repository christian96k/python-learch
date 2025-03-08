from fastapi import  HTTPException, Depends
from sqlalchemy.orm import Session
from models.item_dto import ItemDTO, ItemCreateDTO
from routers.v1.items import get_db
from schemas.items_schema import ItemSchema


async def create_item(item: ItemCreateDTO, db: Session = Depends(get_db)):
    db_item = ItemSchema(value=item.value, active=item.active)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

async def list_items(db: Session = Depends(get_db)):
    items = db.query(ItemSchema).all()
    return items

async def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemSchema).filter(ItemSchema.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


async def edit_item(item: ItemDTO, db: Session = Depends(get_db)):
    db_item = db.query(ItemSchema).filter(ItemSchema.id == item.id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        db_item.value = item.value
        db_item.active = item.active
        db.commit()
        db.refresh(db_item)
    return db_item

async def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemSchema).filter(ItemSchema.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}