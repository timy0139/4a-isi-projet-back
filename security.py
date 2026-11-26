import os
import secrets

import jwt
from pwdlib import PasswordHash

hasher = PasswordHash.recommended()

SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60


def generate_random_password() -> str:
    return secrets.token_urlsafe(10)


def hash_password(password: str) -> str:
    return hasher.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return hasher.verify(plain, hashed)


def create_access_token(user_id: int) -> str:
    payload = {"sub": str(user_id)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> int | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return int(payload["sub"])
    except (jwt.PyJWTError, KeyError, ValueError):
        return None