from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from uuid import uuid4
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from uuid import uuid4
from enum import Enum
from typing import Annotated

# CREATE TABLE IF NOT exists collection (

#     collection_id UUID PRIMARY KEY default gen_random_uuid(),
#     contract_address varchar(64) NOT NULL,
#     collection_name varchar(64),
#     collection_desc Text,
#     collection_image Text,
#     collection_external_link Text,
#     contract_owner varchar(64),

#     decimals Integer NOT NULL,
#     created_at Integer NOT NULL
# );

class BlockchainType(str, Enum):
    binance = "bnb"
    ethereum = "eth"
    polygon = "matic"

ContractAddress = Annotated[
    str,
    Field(
        pattern=r"^0x[a-fA-F0-9]{40}$",
        description="A smart contract address formatted as '0x' followed by 40 hexadecimal characters.",
        examples=["0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b"],
    ),
]

class Collection(BaseModel):
    collection_id: str = Field(default_factory=lambda: str(uuid4()))
    contract_address: ContractAddress
    collection_name: str
    collection_desc: str
    collection_image: HttpUrl
    collection_external_link: HttpUrl
    contract_owner: str
    decimals: int
    created_at: int = Field(default_factory=lambda: int(datetime.now().replace(microsecond=0)))

class NFT(BaseModel):
    description: str
    external_url: HttpUrl
    image: HttpUrl
    name: str
    attributes: dict