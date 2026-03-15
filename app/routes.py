from fastapi import APIRouter

from app.database.models import Contact
from app.services import operations as op

router = APIRouter()

@router.get("/")
def root():
    return "Welcome to Contact Manager"

@router.post("/contacts")
def create_contact(contact: Contact):
    op.create_contact(contact_name=contact.contact_name, 
                      contact_number=contact.contact_number)