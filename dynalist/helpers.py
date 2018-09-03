import keyring

TOKEN_USERNAME = "dynalist"
PERMISSIONS = ["No access", "Read only", "Edit rights", "Manage", "Owner"]

def token_exists():
    if keyring.get_password("system", TOKEN_USERNAME):
        return True
    return False

def set_token(token):
    keyring.set_password("system", TOKEN_USERNAME, token)

def get_token():
    return keyring.get_password("system", TOKEN_USERNAME)

def reset_token():
    keyring.delete_password("system", TOKEN_USERNAME)

