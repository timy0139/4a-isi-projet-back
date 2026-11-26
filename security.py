import secrets

from pwdlib import PasswordHash


hasher = PasswordHash.recommended()


def generate_random_password() -> str:
    return secrets.token_urlsafe(10)


def hash_password(password: str) -> str:
    return hasher.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return hasher.verify(plain, hashed)