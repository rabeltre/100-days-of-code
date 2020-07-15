import unittest

from PythonApplication2.AOne_Mobile_Services.Contact import Contact
from PythonApplication2.AOne_Mobile_Services.DBConection import ContactDBApp


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.contactdbapp = ContactDBApp()

    def test_add_new_contact(self):
        self.contact1 = Contact("Rafael", "", "")
        self.contactdbapp.delete_contact(self.contact1)

        self.contact1.set_type_of_contact("Personal")
        self.contact1.set_phone_call("1234567989")
        self.contactdbapp.add_contact(self.contact1)
        get_contact = self.contactdbapp.find_contact_by_name(self.contact1)

        self.assertEqual(self.contact1.get_name(), get_contact[0][0])
        self.assertEqual(self.contact1.type_of_contact, get_contact[0][1])
        self.assertEqual(self.contact1.get_phone_call(), get_contact[0][2])

    def test_update_existing_contact(self):
        self.contact1 = Contact("Rafael", "Work", "829-380-3284")
        self.contactdbapp.update_contact(self.contact1)
        get_contact = self.contactdbapp.find_contact_by_name(self.contact1)

        self.assertEqual(self.contact1.get_name(), get_contact[0][0])
        self.assertEqual(self.contact1.type_of_contact, get_contact[0][1])
        self.assertEqual(self.contact1.get_phone_call(), get_contact[0][2])

    def test_duplicate_contact(self):
        self.contact1 = Contact("Rafael", "Work", "829-380-3284")
        self.contactdbapp.delete_contact(self.contact1)
        query_result = self.contactdbapp.add_contact(self.contact1)
        self.assertEqual(query_result, True)
        query_result = self.contactdbapp.add_contact(self.contact1)
        self.assertEqual(query_result, False)

    def test_delete_contact(self):
        self.contact1 = Contact("test1", "Work", "7894561423")
        self.contactdbapp.add_contact(self.contact1)

        # Test delete existing contact
        query_result = self.contactdbapp.delete_contact(self.contact1)
        self.assertEqual(query_result, True)

        # Test delete no existing contact
        query_result = self.contactdbapp.delete_contact(self.contact1)
        self.assertEqual(query_result, False)



if __name__ == '__main__':
    unittest.main()

