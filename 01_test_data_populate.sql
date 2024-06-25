-- Populate collection table
INSERT INTO collection (
  collection_id, contract_address, 
  collection_name, collection_desc, 
  collection_image, collection_external_link, 
  contract_owner, decimals, created_at
) 
VALUES 
  (
    '550e8400-e29b-41d4-a716-446655440000', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b', 
    'Game Skins Collection', 'Collection of skins for the game', 
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
VALUES 
  (
    '660e8400-e29b-41d4-a716-446655440020', 'ETH', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0c', 
    '1', 'Skin1', 'Skin-1: Armor with helmet', 
    'http://example.com/skin1.jpg', 
    '{"name": "Skin1", "image": "http://example.com/skin1.jpg", "description": "Description of Skin1", "tokenUri": "tokenURI_value"}', 
    1630636800, 1630636800, '550e8400-e29b-41d4-a716-446655440000'
  ), 
  (
    '770e8400-e29b-41d4-a716-446655440030', 'ETH', '0x2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a0d', 
    '2', 'Skin2', 'Skin-2: Armor with shield', 
    'http://example.com/skin2.jpg', 
    '{"name": "Skin2", "image": "http://example.com/skin2.jpg", "description": "Description of Skin2", "tokenUri": "tokenURI_value"}', 
    1630636800, 1630636800, '550e8400-e29b-41d4-a716-446655440000'
  );

INSERT INTO asset (
  asset_id, asset_type_id, user_wallet, 
  count, extras, updated_at, created_at
) 
VALUES 
  (
    '9a3d3d60-9e0f-4dca-b07e-8f209465e4c1', 
    '660e8400-e29b-41d4-a716-446655440020', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7aaabbb1', 1, '{"variation": "Standard"}', 
    1630636800, 1630636800
  ), 
  (
    'd1992a8d-4f44-4678-af68-8f96b173d1fa', 
    '770e8400-e29b-41d4-a716-446655440030', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7aaabbb1', 1, '{"variation": "Premium"}', 
    1630636800, 1630636800
  ), 
  (
    'fd0f45f5-b3f2-4c77-9a9c-3f1c24cfe19d', 
    '660e8400-e29b-41d4-a716-446655440020', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7cccddd2', 1, '{"variation": "Exclusive"}', 
    1630636800, 1630636800
  ), 
  (
    '2cb4a7ef-b6c0-4d5b-912a-2b4e1abce78a', 
    '770e8400-e29b-41d4-a716-446655440030', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7cccddd2', 1, '{"variation": "Standard"}', 
    1630636800, 1630636800
  ), 
  (
    'e24b9e50-7d34-4c84-8b56-4f4c7ef3d4eb', 
    '770e8400-e29b-41d4-a716-446655440030', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7aaabbb1', 1, '{"variation": "Premium"}', 
    1630636800, 1630636800
  ), 
  (
    '5f5d2f06-22d4-4be3-a53a-bfaa266a5e3f', 
    '660e8400-e29b-41d4-a716-446655440020', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7cccddd2', 1, '{"variation": "Exclusive"}', 
    1630636800, 1630636800
  ), 
  (
    '835e1c6f-3b87-4c28-a57a-67e2f714b7e0', 
    '660e8400-e29b-41d4-a716-446655440020', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7aaabbb1', 1, '{"variation": "Special Edition"}', 
    1630636800, 1630636800
  ), 
  (
    'a14ed6c4-cba6-4333-9517-93e83ce106ff', 
    '770e8400-e29b-41d4-a716-446655440030', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7aaabbb1', 1, '{"variation": "Limited Edition"}', 
    1630636800, 1630636800
  ), 
  (
    '694e90b6-4b04-4f21-8b69-cb39fbb46964', 
    '660e8400-e29b-41d4-a716-446655440020', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7aaabbb1', 1, '{"variation": "Special Edition"}', 
    1630636800, 1630636800
  ), 
  (
    'b728fcd1-3ea5-43a0-bb30-792e464e1c71', 
    '660e8400-e29b-41d4-a716-446655440020', '0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7cccddd2', 1, '{"variation": "Limited Edition"}', 
    1630636800, 1630636800
  );
