# Built-in Modules
import subprocess

# Third Party Modules
from cryptography.fernet import Fernet
from dotenv import dotenv_values

# User-defined modules
import app.database as db

def encrypt(contact_info: int | str):
    """Encrypts the contact number using fernet a symmmetric cipher"""

    if type(contact_info) == int:
        contact_info = contact_info.to_bytes(8,'big')
    else:
        contact_info = contact_info.encode('utf-8')
        
    key = Fernet.generate_key()
    f= Fernet(key)
    encrypted_contact_info = f.encrypt(contact_info)

    return encrypted_contact_info, key

def decrypt(encrypted_contact_data: bytes, key: bytes):
    """Decrypts the contact number using fernet a symmmetric cipher"""

    f = Fernet(key)
    original_contact_data = f.decrypt(encrypted_contact_data)

    return original_contact_data

def stores_contact_num_key_in_env_file(key: bytes, name: str):
    """Stores the Contact Number key in the .env file"""

    name_of_key = f"KEY_OF_{name.upper()}" # Turning to upper case to maintain the format
    
    # decoding the key as would store along with the 'b' as prefix in the database
    key_str = key.decode('utf-8') 
    command = f"dotenv set {name_of_key} {key_str}"
    res = subprocess.run(command, shell=True, capture_output=True)

def stores_email_key_in_env_file(key: bytes, name: str):
    """Stores the Email key in the .env file"""

    name_of_key = f"KEY_OF_EMAIL_{name.upper()}"
    
    # decoding the key as would store along with the 'b' as prefix in the database
    key_str = key.decode('utf-8') 
    command = f"dotenv set {name_of_key} {key_str}"
    res = subprocess.run(command, shell=True, capture_output=True)

def retrieve_contact_num_key_from_env_file(name: str):
    """Retrieves the Contact Number key from the .env file"""

    name_of_key = f"KEY_OF_{name.upper()}"
    dict_of_keys = dotenv_values(".env")

    for key,value in dict_of_keys.items():
        
        if key == name_of_key:
            key_for_contact_number = value
            break
    # encoding the key as decrypt() function expects a bytes object
    key_for_contact_number = key_for_contact_number.encode('utf-8')

    return key_for_contact_number

def retrieve_email_key_from_env_file(name: str):
    """Retrieves th Email key from the .env file"""

    name_of_key = f"KEY_OF_EMAIL_{name.upper()}"
    dict_of_keys = dotenv_values(".env")

    for key,value in dict_of_keys.items():
        
        if key == name_of_key:
            key_for_email = value
            break
        else:
            key_for_email = None
    # encoding the key as decrypt() function expects a bytes object
    if key_for_email != None:
        key_for_email = key_for_email.encode('utf-8')

    return key_for_email




if __name__ == '__main__':
    pass