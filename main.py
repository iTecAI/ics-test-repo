from fastapi import FastAPI
import time

app = FastAPI()

@app.post('/test')
async def post_test():
    return {
        'time': time.time(),
        'method': 'POST'
    }

@app.get('/test')
async def get_test():
    return {
        'time': time.time(),
        'method': 'GET'
    }