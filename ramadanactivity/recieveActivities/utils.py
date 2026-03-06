import base64
import hashlib

from django.conf import settings


def _get_key() -> bytes:
    return hashlib.sha256(settings.SECRET_KEY.encode('utf-8')).digest()


def _xor_cipher(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def encrypt_phone(plain_phone: str) -> str:
    key = _get_key()
    encrypted = _xor_cipher(plain_phone.encode('utf-8'), key)
    return base64.urlsafe_b64encode(encrypted).decode('utf-8')


def decrypt_phone(token: str) -> str:
    key = _get_key()
    encrypted = base64.urlsafe_b64decode(token.encode('utf-8'))
    return _xor_cipher(encrypted, key).decode('utf-8')

