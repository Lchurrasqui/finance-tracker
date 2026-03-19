from pydantic import BaseModel, EmailStr, ConfigDict

class AccountCreate(BaseModel):
    name: str

class AccountResponse(BaseModel):
    id: int
    name: str
    user_id: int
    
    model_config = ConfigDict(from_attributes=True)
