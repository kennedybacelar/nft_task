from datetime import datetime
from enum import Enum
from uuid import uuid4

from pydantic import BaseModel, Field

from .commons import AddressModel


class TransactionType(str, Enum):
    transfer = "transfer"


class TransactionStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    failed = "failed"


class TransferTransactionNFT(BaseModel):
    transaction_id: str = Field(default_factory=lambda: str(uuid4()))
    event_type: TransactionType = TransactionType.transfer
    transaction_status: TransactionStatus
    token_id: int
    from_address: AddressModel
    to_address: AddressModel
    created_at: int = Field(
        default_factory=lambda: int(datetime.now().replace(microsecond=0))
    )


class TransactionResponse(BaseModel):
    transaction_id: str
    event_type: TransactionType
    transaction_status: TransactionStatus
