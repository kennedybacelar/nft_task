from enum import Enum
from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime

class TransactionType(str, Enum):
    transfer = "transfer"

class TransactionStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    failed = "failed"

class Transaction(BaseModel):
    transaction_id: str = Field(default_factory=lambda: str(uuid4()))
    transaction_type: TransactionType
    transaction_status: TransactionStatus
    sender: str
    recipient: str
    amount: int
    created_at: int = Field(default_factory=lambda: int(datetime.now().replace(microsecond=0)))