from typing import List
from fastapi import APIRouter, HTTPException, status

from app import crud, schemas

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=schemas.ItemOut,
             status_code=status.HTTP_201_CREATED)
def create_item(item: schemas.ItemCreate):
    return crud.create_item(item)


@router.get("/", response_model=List[schemas.ItemOut])
def list_items(skip: int = 0, limit: int = 100):
    return crud.get_items(skip=skip, limit=limit)


@router.get("/{item_id}", response_model=schemas.ItemOut)
def read_item(item_id: str):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=schemas.ItemOut)
def update_item(item_id: str, item: schemas.ItemUpdate):
    updated_item = crud.update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: str):
    deleted = crud.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
