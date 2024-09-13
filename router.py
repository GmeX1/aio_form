from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repositories import UserRepository
from schemas import input_schemas
from schemas import output_schemas
import models
from tg_bot import alert_user

router_api = APIRouter()


@router_api.post('/api/register')
async def user_register(user: input_schemas.UserInfoForm, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)

    status = user_repo.create_user(user)
    if type(status) is models.User:
        await alert_user(status)
        return output_schemas.DBUserStatus(status=True)
        # return {'status': True, 'description': None}
    return output_schemas.DBUserStatus(status=False, description=status)
    # return {'status': False, 'description': status}
