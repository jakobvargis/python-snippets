from fastapi import FastAPI, HTTPException, Query
from enum import Enum
from pydantic import BaseModel
from typing import Annotated, Dict, Any


class ModelName(str, Enum):
    alex = "alex"
    sonja = "sonja"
    riddick = "riddick"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


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
    item = next((item for item in fake_items_db if item['item_id'] == item_id), None)
    if not item:
        return HTTPException(status_code=404, detail="Searched item not found")

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

# Create a new item
@app.post('/item_create')
async def create_item(item: Item):
    # Calculate tax as we can access all the attributes of the model object directly:
    item_dict = item.dict()
    if item.tax is not None:
        mrp = item.price + item.tax
        item_dict.update({'mrp' : mrp})
    return item_dict


# update an existing record by adding a new field
@app.put('/items/{item_id}')
async def update_selected_item(item_id: int, item: Item, q: str | None = None):             
    result = {'item_id': item_id, **item.dict()}
    if not result:
        return HTTPException(status_code=404, detail="Searched item not found.")

    if q:
        result.update({'q' : q})

    return result    


# Filter and view data in Fake_data_db where name contains '1;
@app.get('/filteritems')
async def read_filtered_data(q: Annotated[str | None, Query(max_length=50)] = None):
    if q:
        filtered_results = [item for item in fake_items_db if q.lower() in item['name'].lower()]
        return {'items' : filtered_results}
    else:  #if no query is given as left blank
        return  {'items' : fake_items_db}  # returns full list of items


@app.get('/get_exact')
async def get_exact_query(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):
    result: Dict[str, Any] = {'itemz': [{'item_id': 1, 'product': "Raspberry Pi 500"},
                          {'item_id': 2, 'product': "Keyboard & Mouse"}
            ]}
    if q:
        result.update({'q' : q})
    
    return result
    

@app.get('/get_as_list')
async def get_as_list(q: Annotated[list[str] | None, Query()] = None):  #you can also declare it to receive a list of values, or said in another way, to receive multiple values
    query_items = {'q' : q}
    return query_items
