from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str  
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# from_attributes=True --> convierte objetos en JSON usando sus atributos en lugar de sus claves. Esto es útil cuando se trabaja con objetos que no son diccionarios, como los modelos de bases de datos. Al establecer from_attributes=True, Pydantic intentará acceder a los atributos del objeto para convertirlo en JSON, lo que facilita la serialización de objetos complejos.