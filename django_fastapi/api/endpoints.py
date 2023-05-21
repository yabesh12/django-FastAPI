from typing import List

from fastapi import APIRouter
from django.http import JsonResponse
from api import models, schemas


api_router = APIRouter()


@api_router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate):
    item = models.Item.objects.create(**item.dict())

    return item


@api_router.get("/items", response_model=List[schemas.Item])
def read_items():
    items = list(models.Item.objects.all())

    return items

@api_router.put("/item/<id>", response_model=schemas.Item)
def update_item(item: schemas.ItemCreate, id):
    try:
        item_obj = models.Item.objects.get(id=id)
    except models.Item.DoesNotExist:
        raise Exception({"Status":"error", "message":"Item Does not exists"})

    item_obj.title = item.dict().get("title")
    item_obj.description = item.dict().get("description")
    item_obj.save(update_fields=["title", "description"])

    return item_obj

@api_router.delete("/item/<id>",)
def update_item(id):
    try:
        item_obj = models.Item.objects.get(id=id)
    except models.Item.DoesNotExist:
        raise Exception({"Status":"error", "message":"Item Does not exists"})

    item_obj.delete()

    return JsonResponse({"Status":"Success", "message":"Item Successfully deleted"})

