from PythonApplication2.AOne_Mobile_Services.Contact import Contact
import sqlite3


def execute_query(query):
    con = None
    data = None
    try:
        con = sqlite3.connect('contact_app.db')
        cur = con.cursor()
        cur.execute(query)
        data = cur.fetchall()
        if not data:
            con.commit()
    except sqlite3.Error as e:
        print("Database error: %s" % e)
    except Exception as e:
        print("Exception in _query: %s" % e)
    finally:
        if con:
            con.close()
    return data


class ContactDBApp:

    def __init__(self):
        pass

    def add_contact(self, contact):
        if self.check_if_contact_exist(contact):
            return False
        else:
            query = f"INSERT INTO contact_app VALUES ('{contact.get_name()}'," \
                    f" '{contact.get_type_of_contact()}', '{contact.get_phone_call()}')"
            execute_query(query)
            return True

    def update_contact(self, contact):
        if self.check_if_contact_exist(contact):
            query = f"update contact_app set name= '{contact.get_name()}', " \
                    f"type_of_contact='{contact.get_type_of_contact()}'" \
                    f", phone_call= '{contact.get_phone_call()}' where name='{contact.get_name()}'"
            execute_query(query)
            return True
        else:
            return False

    def delete_contact(self, contact):
        if self.check_if_contact_exist(contact):
            query = f"delete from contact_app where name= '{contact.get_name()}'"
            execute_query(query)
            return True
        else:
            return False

    def find_contact_by_name(self, contact):
        query = f"select * from contact_app where name= '{contact.get_name()}'"

        return execute_query(query)

    def find_all_contact(self):
        query = "select * from contact_app"
        return execute_query(query)

    def check_if_contact_exist(self, contact):
        if self.find_contact_by_name(contact):
            return True
        else:
            return False



# Create table
"""
c.execute('''CREATE TABLE contact_app
             (name text, type_of_contact text, phone_call text)''')
"""
