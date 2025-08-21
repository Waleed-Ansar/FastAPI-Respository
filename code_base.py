from db import Stock
from models import Model
from schema import return_items
from fastapi import APIRouter
from bson import ObjectId

router = APIRouter()

def item_helper(item) -> dict:
    item["_id"] = str(item["_id"])
    return item

@router.get("/")
async def display_items():
    stock = Stock.find({})
    items = []
    async for item in stock:
        items.append(item_helper(item))   # convert ObjectId to str
    return items
    
@router.post("/post")
async def add_stock(data: Model):
    await Stock.insert_one(dict(data))
    return data

@router.put("/put/{update_id}")
async def update_stock(update_id: str, data: Model):
    await Stock.find_one_and_update({"_id": ObjectId(update_id)}, {"$set": dict(data)}, return_document=True)

@router.delete("/delete/{delete_id}")
async def delete_from_stock(delete_id: str):
    await Stock.find_one_and_delete({"_id": ObjectId(delete_id)})
