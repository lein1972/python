items = {}

def get_item(item_id: int):
    return items.get(item_id)

def create_item(item_id: int, item: dict):
    items[item_id] = item
    return items[item_id]