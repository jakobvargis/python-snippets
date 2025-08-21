from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alex = "alex"
    sonja = "sonja"
    riddick = "riddick"


app = FastAPI()


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
