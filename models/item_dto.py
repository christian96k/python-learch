from pydantic import BaseModel

class ItemDTO(BaseModel):
    pass
    id: int
    value: str
    active: bool = None

    class Config:
        from_attributes = True

class ItemCreateDTO(BaseModel):
    value: str
    active: bool = None