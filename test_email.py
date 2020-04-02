# import unittest

# import send_inspiration
# from mock import Mock


# class TestEmail(unittest.TestCase):
    
#     def test_get_contacts(self):
#         names = send_inspiration('To', 'From', 'Subject')
#         self.assertEqual('thato','MY_ADDRESS', 'message') == True
    
#     #def test_main(self):

#-------------------
import smtplib,unittest
from unittest import TestCase
from unittest.mock import Mock
from send_inspiration import main
import logging
mock = Mock()

m = mock.Mock()
class Sending_email(unittest.TestCase):
    def setUp(self):
        self.emails = []
    def test_get_contacts(self,*args):
        for i in self.emails:
            self.assertTrue(i == main(),'Incorrect')
        s = 'Theo theo.kobuoe@umuzi.org'
        self.assertEqual(s.split(), ['Theo','theo.kobuoe@umuzi.org'])
        with self.assertRaises(TypeError):
            s.split(2)
            self.assertEqual(len(s.emails), 2)
            self.assertEqual(s.emails[0].frm, 'theo.kobuoe@umuzi.org')
            self.assertEqual(s.emails[0].to, ['newkobuoe@gmail.com'])
            self.assertEqual(s.emails[0].msg, "Here's a random ispiration quote for you!!!!")
            self.assertEqual(m.get_contacts) == False
            
    def test_get_contacts(self):
        names = send_inspiration('To', 'From', 'Subject')
        self.assertEqual('Theo','MY_ADDRESS', 'message') == False

    def tearDown(self):
        self.emails = None
if __name__ == '__main__':
    unittest.main()