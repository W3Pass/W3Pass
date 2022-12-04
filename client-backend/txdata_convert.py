from cryptography.fernet import Fernet
from urllib.parse import urlparse
# import hashlib as hash
import dict_hash as hdict


def getCredentials() -> tuple[str, str, str]:
    # input user data
    domain: str = urlparse(input("enter domain: ")).netloc
    hostname: str = (".".join(domain.split(".")[-2:]))
    email: str = input("enter email:")    
    password: str = input("enter password: ")

    return hostname, email, password
    
def getEncrypted(email: str, password: str, domain: str) -> tuple[tuple[bytes, bytes], bytes]:

    # generate a key for encryption
    key_value = Fernet.generate_key()
    key = Fernet(key_value)
    
    # byte conversion
    byte_email: bytes = bytes(email, 'utf-8')
    byte_password: bytes = bytes(password, 'utf-8')
    byte_domain: bytes = bytes(domain, 'utf-8')

    # encryption process
    encrypt_email: bytes = key.encrypt(byte_email)
    encrypt_password: bytes = key.encrypt(byte_password)

    encrypted_user_data: tuple[bytes, bytes] = encrypt_email, encrypt_password

    return encrypted_user_data, byte_domain

# def getTransactionHash(encrypted_data: tuple[bytes, bytes], domain: str):
#     email = encrypted_data[0]
#     password = encrypted_data[1]

#     user_data = {"domain": domain, "email": email, "password": password}

#     tx_hash: str = hdict.sha256(user_data)

#     return tx_hash

def main():
    domain, email, password = getCredentials()
    encrypted_data = getEncrypted(domain, email, password)
    
    # tx_hash = getTransactionHash(encrypted_data, domain)

    # print(tx_hash)