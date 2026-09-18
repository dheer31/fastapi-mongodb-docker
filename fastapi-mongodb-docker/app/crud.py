from datetime import datetime, timezone
from typing import List, Optional
from bson import ObjectId

from app.database import items_collection
from app import schemas


def serialize_item(item: dict) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item.get("description"),
        "price": item["price"],
        "created_at": item.get("created_at"),
        "updated_at": item.get("updated_at"),
    }


def get_item(item_id: str) -> Optional[dict]:
    if not ObjectId.is_valid(item_id):
        return None

    item = items_collection.find_one({"_id": ObjectId(item_id)})
    return serialize_item(item) if item else None


def get_items(skip: int = 0, limit: int = 100) -> List[dict]:
    items = items_collection.find().skip(skip).limit(limit)
    return [serialize_item(item) for item in items]


def create_item(item: schemas.ItemCreate) -> dict:
    now = datetime.now(timezone.utc)
    item_data = item.model_dump()
    item_data["created_at"] = now
    item_data["updated_at"] = now

    result = items_collection.insert_one(item_data)
    created_item = items_collection.find_one({"_id": result.inserted_id})
    return serialize_item(created_item)


def update_item(item_id: str, item: schemas.ItemUpdate) -> Optional[dict]:
    if not ObjectId.is_valid(item_id):
        return None

    update_data = item.model_dump(exclude_unset=True)
    update_data["updated_at"] = datetime.now(timezone.utc)

    result = items_collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        return None

    return get_item(item_id)


def delete_item(item_id: str) -> bool:
    if not ObjectId.is_valid(item_id):
        return False

    result = items_collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0
