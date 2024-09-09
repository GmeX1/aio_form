from typing import Literal

from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(min_length=1, max_length=255, pattern='^[А-Яа-яA-Za-z -]+$')
    tg: str = Field(min_length=2, max_length=255, pattern='^@[A-Za-z0-9]+$')
    specialty: Literal['Front-end', 'Back-end', 'Design']
