from app.services.encryption import encrypt
from app.services.file_operations import stores_contact_num_key_in_env_file
from app.database.db_operations import create_contact_db

def create_contact(contact_name: str, contact_number: int):
    """Encrypts the contact number, sends the key to the .env file, and sends the contact data to the database"""
    encrypted_contact_number, key = encrypt(contact_number)
    stores_contact_num_key_in_env_file(key, contact_name)
    create_contact_db(contact_name, encrypted_contact_number)    

if __name__ == '__main__':
    create_contact()