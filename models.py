from pydantic import BaseModel

class Model(BaseModel):
    item: str
    price: int