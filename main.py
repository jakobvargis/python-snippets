from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alex = "alex"
    sonja = "sonja"
    riddick = "riddick"


app = FastAPI()

fake_items_db = [
    {"item_id": 1, "name": "Item 1"},
    {"item_id": 2, "name": "Item 2"},
    {"item_id": 3, "name": "Item 3"},
    {"item_id": 4, "name": "Item 4"},
    {"item_id": 5, "name": "Item 5"},
    {"item_id": 6, "name": "Item 6"},
    {"item_id": 7, "name": "Item 7"},
    {"item_id": 8, "name": "Item 8"},
    {"item_id": 9, "name": "Item 9"},
    {"item_id": 10, "name": "Item 10"},
    {"item_id": 11, "name": "Item 11"},
    {"item_id": 12, "name": "Item 12"},
]

@app.get('/')
async def root():
    return {'message': 'Hellow, World'}


@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'Current User'}


@app.get('/users/{user_id}')
async def read_user(user_id: int):
    return {'user_id': user_id}

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name.value.lower() == ModelName.alex.value.lower():
        return {'model_name' : model_name, 'message' : 'This is Alex'}
    
    if model_name is ModelName.riddick:
        return {'model_name' : model_name, 'message' : 'This is Riddick' }
    
    return {'model_name' : model_name, 'message' : 'This is Sonja'}

# There should not be any spaces between file_path:path
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path':file_path}


@app.get('/items')
async def read_items(skip:int = 0, limit:int = -5):
    return fake_items_db[skip:limit]


@app.get('/items/{item_id}')
async def get_specific_item(item_id: int, q: str | None = None, short: bool = False ):
    item = next(item for item in fake_items_db if item['item_id'] == item_id)
    if not item:
        return {'message' : 'Item not found.'}

    # Sample of URL: http://127.0.0.1:8000/items/4?q=Hello&short=false
    # Create a copy of the item element in result so changes to result dont effect original item
    result = item.copy()

    # Add to result if query is provided
    if q:
        result['q'] = q

    # If short is False → not short is True, so the code block is executed.
    # If short is True → not short is False, so the code block is skipped.
    # Action adds a description if short is false
    if not short:
        result['description'] = "This is a detailed description"

    return result
