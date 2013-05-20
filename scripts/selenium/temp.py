from selenium import selenium
import unittest, time, re

class temp(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://www.tumblr.com/")
        self.selenium.start()
    
    def test_temp(self):
        sel = self.selenium
        sel.open("/login")
        sel.type("id=signup_password", "Drtisdrt??")
        sel.click("id=signup_forms_submit")
        sel.wait_for_page_to_load("30000")
        sel.type("id=signup_email","james.a.munsch@gmail.com")
	<td>type</td>
	<td>id=signup_email</td>
	<td>james.a.munsch@gmail.com</td>

