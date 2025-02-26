from cryptography.fernet import Fernet
import base64
from django.conf import settings


def encrypt(txt) -> str:
    '''
        Encrypt data
    '''

    try:
        txt = str(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception:
        return None


def decrypt(txt) -> str:
    '''
        Decrypt data
    '''

    try:
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text
    except Exception:
        return None
