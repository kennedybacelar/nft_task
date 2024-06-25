# NFT TASK

This project is a RESTful API - single endpoint

## Dependencies

This project relies on the following dependencies:

- [Poetry](https://python-poetry.org/): A dependency manager for Python projects. Install it to manage project dependencies and virtual environments.
- [Docker](https://www.docker.com/): A containerization platform that allows you to package and distribute applications and their dependencies as containers.

Ensure that both Poetry and Docker are installed on your system before proceeding with the setup and usage of this project.

1. Clone the repository:

   ```bash
   git clone git clone https://github.com/kennedybacelar/nft_task

2. Navigate to the project directory:

    ```bash
    cd qorpo-crypto-api
    
3. Install dependencies using Poetry:

    ```bash
    poetry install

## Usage


### Running the API

You can run the API in multiple ways:

1. As a Python Module:

    ```bash
    python -m run

2. Using Docker:

    ```bash
    docker-compose up

### Running Tests With Docker

Automatic tests not implemented

Manual testing 

for example:

curl -X POST http://localhost:5000/asset/transfer -H "Content-Type: application/json" -d '{"token_id": 123456, "blockchain_symbol": "bnb", "from_address": "0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7aaabbb1", "to_address": "0x1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7cccddd2"}'

### Response type

{
  "TransactionResponse": {
    "transaction_id": "string",
    "event_type": "TransactionType",
    "transaction_status": "TransactionStatus",
    "sender_count": "float",
    "receiver_count": "float"
  }
}