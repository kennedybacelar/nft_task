from sqlalchemy import (JSON, Column, Float, ForeignKey, Integer, String, Text,
                        func)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class BaseMixin:
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Collection(Base):
    __tablename__ = "collection"
    collection_id = Column(UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    contract_address = Column(String(64), nullable=False)
    collection_name = Column(String(64))
    collection_desc = Column(Text)
    collection_image = Column(Text)
    collection_external_link = Column(Text)
    contract_owner = Column(String(64))
    decimals = Column(Integer, nullable=False)
    created_at = Column(Integer, nullable=False)

    asset_types = relationship("AssetType", back_populates="collection")


class AssetType(Base):
    __tablename__ = "asset_type"
    asset_type_id = Column(UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    blockchain = Column(String(8), nullable=False)
    contract_address = Column(String(54), nullable=False)
    token_id = Column(String(256))
    name = Column(String(256), default="N/A")
    description = Column(Text, default="N/A")
    image_url = Column(Text, default="N/A")
    asset_type_metadata = Column(JSON, default={})
    updated_at = Column(Integer, nullable=False)
    created_at = Column(Integer, nullable=False)
    collection_id = Column(UUID(as_uuid=True), ForeignKey("collection.collection_id"))

    collection = relationship("Collection", back_populates="asset_types")
    assets = relationship("AssetTable", back_populates="asset_type")


class AssetTable(Base, BaseMixin):
    __tablename__ = "asset"
    asset_id = Column(UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    asset_type_id = Column(UUID(as_uuid=True), ForeignKey("asset_type.asset_type_id"), nullable=False)
    user_wallet = Column(String(256), nullable=False)
    count = Column(Float, default=0)
    extras = Column(JSON, default={})
    updated_at = Column(Integer, nullable=False)
    created_at = Column(Integer, nullable=False)

    asset_type = relationship("AssetType", back_populates="assets")


class Transaction(Base):
    __tablename__ = "transaction"
    transaction_id = Column(UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    type = Column(String(64), nullable=False)
    description = Column(Text)
    delta = Column(Float, nullable=False)
    created_at = Column(Integer, nullable=False)
    data = Column(JSON, default={})
    user_wallet = Column(String(64), nullable=False)
    contract_address = Column(String(64), nullable=False)
    token_id = Column(String(256))
    name = Column(String(32), nullable=False)
