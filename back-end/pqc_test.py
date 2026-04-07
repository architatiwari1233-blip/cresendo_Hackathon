import hashlib

def generate_keys():
    public_key = "public_key_simulated"
    secret_key = "secret_key_simulated"
    return public_key, secret_key

def sign(message, secret_key):
    return hashlib.sha256((message + secret_key).encode()).hexdigest()

def verify(message, signature, secret_key):
    expected = hashlib.sha256((message + secret_key).encode()).hexdigest()
    return expected == signature


# Test
public_key, secret_key = generate_keys()

message = "Hello QuantumShield"

signature = sign(message, secret_key)

print("Message:", message)
print("Signature:", signature)

if verify(message, signature, secret_key):
    print("✅ Signature is VALID (Quantum Secure Simulation)")
else:
    print("❌ Signature INVALID")
