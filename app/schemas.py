from pydantic import BaseModel

class ContactEntry(BaseModel):
    contact_name : str
    contact_number : int