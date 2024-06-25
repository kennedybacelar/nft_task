from datetime import datetime
from enum import Enum
from uuid import uuid4
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl

from .commons import AddressModel, BlockchainType


class Collection(BaseModel):
    collection_id: str = Field(default_factory=lambda: str(uuid4()))
    contract_address: AddressModel
    collection_name: str
    collection_desc: str
    collection_image: HttpUrl = Field(default="https://via.placeholder.com/150")
    collection_external_link: HttpUrl = Field(default="https://via.placeholder.com/150")
    contract_owner: str
    decimals: int
    created_at: datetime = Field(default_factory=lambda: int(datetime.now().replace(microsecond=0)))


class AssetType(BaseModel):
    asset_type_id: str = Field(default_factory=lambda: str(uuid4()))
    blockchain: BlockchainType
    contract_address: AddressModel
    token_id: int
    name: str = "N/A"
    description: str = "N/A"
    image_url: Optional[HttpUrl] = None
    asset_type_metadata: dict = Field(default_factory=dict)
    updated_at: datetime = Field(default_factory=lambda: int(datetime.now().replace(microsecond=0)))
    created_at: datetime = Field(default_factory=lambda: int(datetime.now().replace(microsecond=0)))
    collection_id: str