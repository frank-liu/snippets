from selenium import selenium
import unittest, time, re

class twitter_login(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox", "https://m.twitter.com/")
        self.selenium.start()
    
    def test_twitter_login(self):
        sel = self.selenium
        time.sleep(3)
        sel.open("/")
        sel.wait_for_page_to_load("30000")
#        sel.click("//view[@id='view-old-front']/content/div/div/div[3]/a[2]/span")
        sel.wait_for_page_to_load("30000")
        sel.mouse_move("id=username")
        sel.click("id=username")
        sel.type("id=username", "james.a.munsch@gmail.com")
        sel.mouse_move("id=password")
        sel.click("id=password")
        sel.type("id=password", "Drtisdrt??")
        sel.click("id=signupbutton")
        sel.wait_for_page_to_load("30000")
        sel.click("css=i.navIcon.composeIcon")
        sel.click("css=textarea.tweet-box-textarea.userselect")
        sel.type("css=textarea.tweet-box-textarea.userselect", "selenium - mobile test. cause twitter api is ruff.")
        sel.click("link=Tweet")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
