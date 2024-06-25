CREATE TABLE IF NOT EXISTS collection (
    collection_id UUID PRIMARY KEY default gen_random_uuid(),
    contract_address varchar(64) NOT NULL,
    collection_name varchar(64),
    collection_desc Text,
    collection_image Text,
    collection_external_link Text,
    contract_owner varchar(64),
    decimals integer NOT NULL,
    created_at integer NOT NULL
);

CREATE TABLE IF NOT EXISTS asset_type (
    asset_type_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    blockchain varchar(8) NOT NULL,
    contract_address varchar(54) NOT NULL,
    token_id varchar(256),
    name varchar(256) DEFAULT 'N/A',
    description Text DEFAULT 'N/A',
    image_url Text DEFAULT 'N/A',
    asset_type_metadata JSONB DEFAULT '{}',
    updated_at Integer NOT NULL,
    created_at Integer NOT NULL,
    collection_id UUID,
    FOREIGN KEY (collection_id) REFERENCES collection(collection_id)
);

CREATE TABLE IF NOT EXISTS nft_asset (
    asset_id UUID PRIMARY KEY default gen_random_uuid(),
    asset_type_id UUID NOT NULL,
    user_wallet varchar(256) NOT NULL,
    count Float NOT NULL DEFAULT 0,
    extras jsonb DEFAULT '{}'::jsonb,
    updated_at integer NOT NULL,
    created_at integer NOT NULL,
    FOREIGN KEY (asset_type_id) REFERENCES asset_type(asset_type_id)
);


CREATE TABLE IF NOT exists transaction (
    transaction_id UUID PRIMARY KEY default gen_random_uuid(),
    type varchar(64) NOT NULL,
    description TEXT,
    delta Float NOT NULL,
    created_at Integer NOT NULL,
    data jsonb DEFAULT '{}',

    user_wallet varchar(64) NOT NULL,
    contract_address varchar(64) NOT NULL,

    token_id varchar(256),
    name varchar(32) NOT NULL
);
CREATE INDEX transaction_id_index on transaction(transaction_id);