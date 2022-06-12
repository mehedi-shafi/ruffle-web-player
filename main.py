from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import json
import os
import sys

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

with open('config.json', 'rb') as file:
    config = json.load(file)

if not os.path.exists(config['data_dir']):
    print('Data Directory ERROR!')
    sys.exit(2)


FILES = [f for f in os.listdir(config['data_dir']) if os.path.isfile(os.path.join(config['data_dir'], f))]

@app.get('/')
async def index():
    return FileResponse('index.html')


@app.get('/files')
def get_file_list():
    return {'data': FILES}