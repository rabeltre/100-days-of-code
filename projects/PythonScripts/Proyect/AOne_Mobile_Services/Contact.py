class Contact:

    def __init__(self, name="", type_of_contact="", phone_call=""):
        self.name = name
        self.type_of_contact = type_of_contact
        self.phone_call = phone_call

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type_of_contact(self):
        return self.type_of_contact

    def set_type_of_contact(self, type_of_contact):
        self.type_of_contact = type_of_contact

    def get_phone_call(self):
        return self.phone_call

    def set_phone_call(self, phone_call):
        self.phone_call = phone_call

