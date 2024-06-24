from datetime import datetime
from enum import Enum
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

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
    transaction_status: TransactionStatus = TransactionStatus.pending
    token_id: int
    from_address: AddressModel
    to_address: AddressModel
    created_at: datetime = datetime.now().replace(microsecond=0)

    model_config = ConfigDict(json_encoders={AddressModel: str})


class TransactionResponse(BaseModel):
    transaction_id: str
    event_type: TransactionType
    transaction_status: TransactionStatus
