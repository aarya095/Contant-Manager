from pydantic import BaseModel

class CreateContact(BaseModel):
    contact_name : str
    contact_number : int
