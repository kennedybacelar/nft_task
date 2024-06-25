-- Populate collection table
INSERT INTO collection (
  collection_id, contract_address, 
  collection_name, collection_desc, 
  collection_image, collection_external_link, 
  contract_owner, decimals, created_at
) 
VALUES 
  (
    'c1', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b', 'Game Skins Collection', 
    'Collection of skins for the game', 
    'http://example.com/image.jpg', 
    'http://example.com/collection', 
    'owner123', 18, 1630636800
  );
-- Populate asset_type table
INSERT INTO asset_type (
  asset_type_id, blockchain, contract_address, 
  token_id, name, description, image_url, 
  asset_type_metadata, updated_at, 
  created_at, collection_id
) 
VALUES (
  'a1', 'ETH', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0c', 
  '1', 'Skin1', 'Skin-1: Armor with helmet', 
  'http://example.com/skin1.jpg', 
  '{"name": "Skin1", "image": "http://example.com/skin1.jpg", "description": "Description of Skin1", "tokenUri": "tokenURI_value"}', 
  1630636800, 1630636800, 'c1'
),
(
  'a2', 'ETH', '0x2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a0d', 
  '2', 'Skin2', 'Skin-2: Armor with shield', 
  'http://example.com/skin2.jpg', 
  '{"name": "Skin2", "image": "http://example.com/skin2.jpg", "description": "Description of Skin2", "tokenUri": "tokenURI_value"}', 
  1630636800, 1630636800, 'c1'
);
