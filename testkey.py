import secrets

def generate_key():
    return secrets.token_hex(16)

key = generate_key()
print(key)