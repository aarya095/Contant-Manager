from fastapi import FastAPI, HTTPException

from app.schemas import Contact

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to Contact Manager"

@app.post("/contacts")
def create_contact(contact : Contact):
    if validators.email(contact.email) != True:
        raise HTTPException(status_code=400, detail="Please provide a valid email.")
    else:
        
        return contact
    
