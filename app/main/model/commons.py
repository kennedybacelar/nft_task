from enum import Enum
from typing import Annotated

from pydantic import Field

AddressModel = Annotated[
    str,
    Field(
        pattern=r"^0x[a-fA-F0-9]{40}$",
        description="A smart contract address formatted as '0x' followed by 40 hexadecimal characters.",
        examples=["0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b"],
    ),
]


class BlockchainType(str, Enum):
    binance = "bnb"
    ethereum = "eth"
    polygon = "matic"
