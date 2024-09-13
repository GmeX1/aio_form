from pydantic import BaseModel, Field, StrictBool


class DBUserStatus(BaseModel):
    status: bool = StrictBool()
    description: str = Field(default=None)
