from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repository import UserRepository
import schemas
import models
from tg_bot import alert_user

router_api = APIRouter()


@router_api.post('/api/register')
async def user_register(user: schemas.User, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)

    status = user_repo.create_user(user)
    if type(status) is models.User:
        await alert_user(status)
        return {'status': True, 'description': None}
    return {'status': False, 'description': status}
