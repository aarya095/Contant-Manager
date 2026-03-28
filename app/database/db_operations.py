from app.database.database import engine
from app.database.models import Contact

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select, delete

def create_contact_db(contact_name: str, encrypted_contact_number: bytes):

    with Session(engine) as session:

        contact_data = Contact(contact_name = contact_name, contact_number = encrypted_contact_number)
        session.add(contact_data)
        session.commit()

    print("Entry created")

def view_contacts():

    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = select(Contact)

    results = session.execute(stmt).all()
    print(results)

    for row in results:
        # row is a Row object, you can access the User object directly
        contact_entry = row[0]
        print(contact_entry)
        print(contact_entry.contact_name, contact_entry.contact_number)

    session.close()
    print("Code block complete")

def empty_database_tables(session):

    Session = sessionmaker(bind=engine)
    session = Session() 
    stmt = delete(Contact)

    session.execute(stmt.execution_options(synchronize_session="fetch"))
    print(f"Cleared table: {Contact.__tablename__}")

    session.commit()
    
if __name__ == '__main__':
    create_contact_db("Aarya",b'gAAAAABptliCAHsPyXXjDcQjqtQLoqwiEaIgZ1ZxiZykUGVk1so4Pr4c30AUM-uOIeJmkXURSzd_VQuaFgEhyzAXvAzTDWoxrg==')
    #view_contacts()