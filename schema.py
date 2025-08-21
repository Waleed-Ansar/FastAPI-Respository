def individual_item(item) -> dict:
    return {
        "id": str(item["_id"]),
        "Item": item["item"],
        "Price": item["price"]
    }

def return_items(items) -> list:
    return [individual_item(item) for item in items]