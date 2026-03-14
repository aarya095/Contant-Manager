from app.database.database import engine
from app.database.models import Contact

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select

def create_user():

    with Session(engine) as session:
        contact1 = Contact(
            contact_name="spongebob",
            contact_number=b'gAAAAABptTYnumd8QXeZxekbZkMW5txmcWdYeEc-v-H6ZPMUC9RMRC4uK3qEX2k2Z0BGVYcwXHja7QwVx2RQ7EtBiW0juo6AVA=='
        )

        session.add(contact1)
        session.commit()

    print("Entry created")

def view_contacts():

    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = select(Contact)

    # Execute the statement and fetch all results
    results = session.execute(stmt).all()
    print(results)

    # 3. Process the results
    for row in results:
        # row is a Row object, you can access the User object directly
        contact_entry = row[0]
        print(contact_entry)
        print(contact_entry.contact_name, contact_entry.contact_number)

    session.close()
    print("Code block complete")

if __name__ == '__main__':
    create_user()
    view_contacts()