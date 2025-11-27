import re
import modules.database as db
import modules.get_and_validate_user_input as get_and_validate

def create_contact():
    """Creates an entry of contact"""
    name_input = get_and_validate.get_and_validate_input_name()
    contact_num_input = get_and_validate.get_and_validate_input_number()
    email_input = get_and_validate.get_and_validate_input_email()

    conn = db.connect_db()
    cur = conn.cursor()

    cur.execute("insert into contacts VALUES (?,?,?)", \
                (name_input, contact_num_input, email_input))
    conn.commit()
    print(f"Contact for {name_input} created successfully!")
    conn.close()

def view_contact():
    """View existing contacts"""
    conn = db.connect_db()
    cur = conn.cursor()

    cur.execute("select * from contacts")
    contacts_data = cur.fetchall()
    
    index = 1
    for contact_data in contacts_data:
        print(f"\n({index})", end='')
        print(f" Name: {contact_data[0]}")
        print(f"    Contact Number: {contact_data[1]}")
        print(f"    Email: {contact_data[2]}")
        index += 1
    conn.close()

def update_contact():
    """Updates the contact information"""
    conn = db.connect_db()
    cur = conn.cursor()

    cur.execute("select * from contacts")
    contacts_data = cur.fetchall()
    index = 1
    for contact_data in contacts_data:
        print(f"\n({index})", end='')
        print(f" Name: {contact_data[0]}")
        index += 1
    update_name_input = input("\nEnter contact name you want to update? \n").lower().strip()

    name_input = get_and_validate.get_and_validate_input_name()
    contact_num_input = get_and_validate.get_and_validate_input_number()
    email_input = get_and_validate.get_and_validate_input_email()

    cur.execute("update contacts set name = ?, contact_number = ?, " \
                "email = ? where name = ?", (name_input, contact_num_input, 
                                              email_input, update_name_input)) 

    conn.commit()
    print(f"Contact for {name_input} updated successfully!")
    conn.close()

def delete_contact():
    """Deletes the contact entry"""
    conn = db.connect_db()
    cur = conn.cursor()

    cur.execute("select * from contacts")
    contacts_data = cur.fetchall()
    
    index = 1
    for contact_data in contacts_data:
        print(f"\n({index})", end='')
        print(f" Name: {contact_data[0]}")
        index += 1

    name_input = input("\nEnter contact name you want to delete? \n").lower().strip()

    cur.execute("delete from contacts where name = ?", (name_input,))
    conn.commit()

    print(f"\nContact for '{name_input}' deleted successfully!")
    conn.close()

def search_name():
    """Search operation to search for a specific name 
    from the list of already existing names and get the contact information"""

    already_existing_names_list = get_and_validate.generate_list_of_already_used_names()
    user_input_for_search = input("Enter the name you want to search: ")

    matched_cases_list = [] # list to store the names where input has matched 
    for name in already_existing_names_list:
        # Loops through the already_existing_names_list and matching using re.search function
        match_case = re.search(user_input_for_search, name, re.IGNORECASE) # Ignoring upper/lower case for better chances       
        if match_case:
            matched_cases_list.append(name)
        if match_case == None:
            pass

    conn = db.connect_db()
    cur = conn.cursor()

    for name in matched_cases_list:
        cur.execute("select * from contacts where name = ?",(name,))
        contact_data = cur.fetchone()
        print(f"\nName: {contact_data[0]}")
        print(f"Contact Number: {contact_data[1]}")
        print(f"Email: {contact_data[2]}")

    conn.close()
        
if __name__ == '__main__':
    search_name()