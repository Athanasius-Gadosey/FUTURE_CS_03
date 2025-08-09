import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import secrets

MASTER_KEY = os.getenv('MASTER_KEY', 'change_this_master_key').encode()

def derive_key(salt):
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        info=b'file_encryption',
        backend=default_backend()
    )
    return hkdf.derive(MASTER_KEY)

def encrypt_file(fileobj, out_path):
    salt = secrets.token_bytes(16)
    key = derive_key(salt)
    nonce = secrets.token_bytes(12)
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce),
        backend=default_backend()
    ).encryptor()
    data = fileobj.read()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    with open(out_path, 'wb') as f:
        f.write(salt + nonce + encryptor.tag + ciphertext)

def decrypt_file(path):
    with open(path, 'rb') as f:
        salt = f.read(16)
        nonce = f.read(12)
        tag = f.read(16)
        ciphertext = f.read()
    key = derive_key(salt)
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce, tag),
        backend=default_backend()
    ).decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    decrypted_path = path + ".dec"
    with open(decrypted_path, 'wb') as f:
        f.write(plaintext)
    return decrypted_path

def list_files(folder):
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

