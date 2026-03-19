
from pydantic import BaseModel, ConfigDict
from typing import Optional
from app.models.transaction import TransactionType
from datetime import datetime
from decimal import Decimal

class TransactionCreate(BaseModel):
    amount: Decimal
    description: Optional[str] = None
    type: TransactionType
    date: datetime

class TransactionResponse(BaseModel):
    id: int
    amount: Decimal
    description: Optional[str] = None
    type: TransactionType
    date: datetime
    category_id: int
    account_id: int
    model_config = ConfigDict(from_attributes=True)