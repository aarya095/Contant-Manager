from fastapi import APIRouter

from app.schemas import CreateContact
from app.services import operations as op

router = APIRouter()

@router.get("/")
def root():
    return "Welcome to Contact Manager"

@router.post("/contacts")
def create_contact(contact: CreateContact):
    op.create_contact(contact_name=contact.contact_name, 
                      contact_number=contact.contact_number)