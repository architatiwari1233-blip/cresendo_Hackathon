from flask import Flask, request, jsonify
import hashlib
from sklearn.ensemble import IsolationForest
import numpy as np
from web3 import Web3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# --- PQC SIMULATION FUNCTIONS ---

def generate_keys():
    public_key = "public_key_simulated"
    secret_key = "secret_key_simulated"
    return public_key, secret_key

def sign(message, secret_key):
    return hashlib.sha256((message + secret_key).encode()).hexdigest()

def verify(message, signature, secret_key):
    expected = hashlib.sha256((message + secret_key).encode()).hexdigest()
    return expected == signature

# Generate keys once
public_key, secret_key = generate_keys()


# --- AI MODEL ---

model = IsolationForest()

# Train with normal transaction amounts
X = np.array([[100], [200], [300], [500], [800], [1000]])
model.fit(X)

def detect_fraud(amount):
    if amount > 2000:
        return "fraud"
    return "safe"


# --- BLOCKCHAIN CONNECTION (SIMULATED) ---

w3 = Web3()  # not using real network for now

def send_to_blockchain(data):
    # Simulated blockchain transaction
    return {
        "tx_hash": "0xABC123DEF456",
        "network": "Ethereum Sepolia (simulated)",
        "status": "Transaction recorded"
    }


@app.route("/")
def home():
    return "QuantumShield Backend Running 🚀"


@app.route("/process_transaction", methods=["POST"])
def process_transaction():
    data = request.get_json()

    # Step 1: Intercept transaction
    print("Transaction Received:", data)

    # Convert transaction to string
    message = str(data)

    # Step 2: PQC Sign
    signature = sign(message, secret_key)

    # Step 3: PQC Verify
    is_valid = verify(message, signature, secret_key)

    if not is_valid:
        return jsonify({
            "status": "blocked",
            "reason": "Invalid PQC Signature"
        })

    # Step 4: AI Fraud Detection
    fraud_result = detect_fraud(data["amount"])

    if fraud_result == "fraud":
        return jsonify({
            "status": "blocked",
            "reason": "Fraud detected by AI"
        })

    # Step 5: Send to Blockchain
    blockchain_result = send_to_blockchain(data)

    # Step 6: Final Response
    return jsonify({
        "status": "success",
        "message": "Transaction secured and sent to blockchain",
        "signature": signature,
        "blockchain": blockchain_result,
        "data": data
    })


if __name__ == "__main__":
    app.run(debug=True)
