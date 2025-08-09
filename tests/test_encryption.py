import os
from app.utils import encrypt_file, decrypt_file

def test_encrypt_decrypt(tmp_path):
    sample_text = b"Hello World"
    sample_file = tmp_path / "test.txt"
    sample_file.write_bytes(sample_text)

    encrypted_path = tmp_path / "test.enc"
    with open(sample_file, 'rb') as f:
        encrypt_file(f, encrypted_path)

    decrypted_path = decrypt_file(encrypted_path)
    with open(decrypted_path, 'rb') as f:
        decrypted_data = f.read()
    assert decrypted_data == sample_text
