from fastapi import APIRouter
from ..models.item import Item
from ..services import item_service

router = APIRouter()

@router.get("/{item_id}")
def read_item(item_id: int):
    return item_service.get_item(item_id)

@router.post("/{item_id}")
def create_item(item_id: int, item: Item):
    return item_service.create_item(item_id, item.dict())