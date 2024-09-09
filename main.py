from fastapi import FastAPI

from schemas import User

app = FastAPI()


@app.post('/register')
async def user_register(user_json: User):
    if user_json:
        return f'{user_json}'
