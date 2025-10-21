# generate_wallet.py
from solana.keypair import Keypair
from solana.rpc.api import Client
import base58
import json
import os

RPC_URL = os.environ.get("RPC_URL", "https://api.devnet.solana.com")

kp = Keypair()
pubkey = str(kp.public_key)
secret_bytes = bytes(kp.secret_key)
secret_b58 = base58.b58encode(secret_bytes).decode()

print("=== NEW SOLANA WALLET ===")
print("Public key:", pubkey)
print("Private key (base58):", secret_b58)
print()

json_arr = list(secret_bytes)
with open("bot-keypair.json", "w") as f:
    json.dump(json_arr, f)

print("Saved to bot-keypair.json ✅")
print("\nCopy this into your .env file:")
print(f"PRIVATE_KEY={secret_b58}")
print(f"RPC_URL={RPC_URL}")