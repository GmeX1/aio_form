from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import schemas
import models


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: schemas.User):
        new_user = models.User(name=user.name, tg=user.tg, specialty=user.specialty)
        try:
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
        except IntegrityError:
            return f'{new_user.tg} is already registered!'
        return new_user

    def get_user_by_id(self, user_id: int):
        pass
