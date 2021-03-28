from typing import Optional

from pydantic import BaseModel


class CreateSchema(BaseModel):
    external_id: Optional[str]
    email: str
    first_name: str
    last_name: str
    phone_number: Optional[str]
    role_code: Optional[str]
