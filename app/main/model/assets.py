from datetime import datetime
from typing import Optional, Union
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, HttpUrl

from .commons import AddressModel, BlockchainType


class CollectionModel(BaseModel):
    collection_id: str = Field(default_factory=lambda: str(uuid4()))
    contract_address: AddressModel
    collection_name: str
    collection_desc: str
    collection_image: HttpUrl = Field(default="https://via.placeholder.com/150")
    collection_external_link: HttpUrl = Field(default="https://via.placeholder.com/150")
    contract_owner: str
    decimals: int
    created_at: datetime = Field(default_factory=lambda: int(datetime.now().timestamp()))


class AssetTypeModel(BaseModel):
    asset_type_id: str = Field(default_factory=lambda: str(uuid4()))
    blockchain: BlockchainType
    contract_address: AddressModel
    token_id: int
    name: str = "N/A"
    description: str = "N/A"
    image_url: Optional[HttpUrl] = None
    asset_type_metadata: dict = Field(default_factory=dict)
    updated_at: datetime = Field(default_factory=lambda: int(datetime.now().timestamp()))
    created_at: datetime = Field(default_factory=lambda: int(datetime.now().timestamp()))
    collection_id: str


class AssetModel(BaseModel):
    asset_id: Union[UUID, str] = Field(default_factory=lambda: str(uuid4()))
    asset_type_id: Union[UUID, str]
    user_wallet: AddressModel
    created_at: datetime = Field(default_factory=lambda: int(datetime.now().timestamp()))
    updated_at: datetime = Field(default_factory=lambda: int(datetime.now().timestamp()))
    count: float = 1.0
