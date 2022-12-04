from cryptography.fernet import Fernet
from urllib.parse import urlparse
from web3 import Web3
import maskpass as mask
import random as rm

#  add credential id in byte-32

def getCredentials() -> tuple[str, str, str, bytes, str]:
    # input user data
    key_value = Fernet.generate_key()
    credential_id: str = str(rm.randint(1,100))
    domain: str = urlparse(input("enter domain: ")).netloc
    hostname: str = (".".join(domain.split(".")[-2:]))
    email: str = input("enter email: ")    
    password: str = mask.askpass(mask="*")

    return hostname, email, password, key_value, credential_id
    
def getEncrypted(byte_key: bytes, domain: str, email: str, password: str) -> tuple[tuple[bytes, bytes], bytes]:
    # generate a key for encryption
    key = Fernet(byte_key)

    # byte conversion
    byte_email: bytes = bytes(email, 'utf-8')
    byte_password: bytes = bytes(password, 'utf-8')
    byte_domain: bytes = bytes(domain, 'utf-8')

    # encryption process
    encrypt_email: bytes = key.encrypt(byte_email)
    encrypt_password: bytes = key.encrypt(byte_password)

    encrypted_user_data: tuple[bytes, bytes] = encrypt_email, encrypt_password

    return encrypted_user_data, byte_domain

def getDecrypted(byte_key: bytes, domain: bytes, email: bytes, password: bytes) -> tuple[str, str, str]:
    key = Fernet(byte_key)

    #  decode domain
    decode_domain: str = domain.decode()

    # decode email
    decrypt_email: bytes = key.decrypt(email)
    decode_email: str = decrypt_email.decode()

    # decode password
    decrypt_password: bytes = key.decrypt(password)
    decode_password: str = decrypt_password.decode()

    # user credentials
    return decode_domain, decode_email, decode_password

# check byte 32 or 64?
def getTransactionInfo(credential_id: bytes, domain: bytes, email: bytes, password: bytes) -> str:
    transaction_info: str = f'''
    Function: addCredentials()
    
    MethodID: 0xcf11deea
    [0]: "{credential_id}"
    [1]: "{domain}"
    [2]: "{email}"
    [3]: "{password}"
    '''
    return transaction_info

def getTransactionData(transaction_info: str):
    hex_tx_data = Web3.toHex(text=transaction_info)
    return hex_tx_data
    

if __name__ == "__main__":
    domain, email, password, byte_key, credential_id = getCredentials()
    encrypted_data = getEncrypted(byte_key, domain, email, password)
    # print("<--------------------------------------------------->")
    # print("Encrypted Email Byte-Code:", encrypted_data[0][0])
    # print("Encrypted Password Byte-Code:", encrypted_data[0][1])
    # print("Trimmed Domain Byte-Code:", encrypted_data[1])
    e_domain = encrypted_data[1]
    e_email = encrypted_data[0][0]
    e_password = encrypted_data[0][1]
    # print("<--------------------------------------------------->")
    # decrypted_data = getDecrypted(byte_key, encrypted_data[1], encrypted_data[0][0], encrypted_data[0][1])
    # print("Domain:", decrypted_data[0])
    # print("Email:", decrypted_data[1])
    # print("Password:", decrypted_data[2])
    # print("<--------------------------------------------------->")
    encode_credential_id: bytes = bytes(credential_id, "utf-8")

    transaction_info: str = getTransactionInfo(encode_credential_id, e_domain, e_email, e_password)
    print(transaction_info)
    tx_hex = getTransactionData(transaction_info)
    print(tx_hex)