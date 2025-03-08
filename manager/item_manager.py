from services.items_service import (
    create_item,
    list_items,
    get_item,
    edit_item,
    delete_item
)
from models.item_dto import ItemCreateDTO, ItemDTO
from sqlalchemy.orm import Session

class ItemsManager:
    def __init__(self, db: Session):
        self.db = db  # Il manager riceve il database dalla dependency injection

    async def manage_create_item(self, item: ItemCreateDTO):
        return await create_item(item, self.db)

    async def manage_list_items(self):
        return await list_items(self.db)

    async def manage_get_item(self, item_id: int):
        return await get_item(item_id, self.db)

    async def manage_edit_item(self, item: ItemDTO):
        return await edit_item(item, self.db)

    async def manage_delete_item(self, item_id: int):
        return await delete_item(item_id, self.db)
