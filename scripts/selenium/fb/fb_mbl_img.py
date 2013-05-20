from selenium import selenium
import unittest, time, re, os

class fb_mbl_img(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://m.facebook.com/")
        self.selenium.start()
    
    def test_fb_mbl_img(self):
        sel = self.selenium
        sel.open("")
        sel.type("name=email", "james.a.munsch@gmail.com")
        sel.type("name=pass", "Drtisdrt??")
        sel.click("name=login")
        sel.wait_for_page_to_load("30000")
        time.sleep(15)

        for files in os.listdir("/home/local/Pictures/101CANON/smaller"):
            try:
                sel.open("/?_rdr")
                sel.click("link=More Options")
                sel.wait_for_page_to_load("30000")
                sel.click("link=Upload Photo")
                sel.wait_for_page_to_load("30000")
                sel.type("name=file1", "/home/local/Pictures/101CANON/smaller/"+files)
                time.sleep(5)
                try:
                    sel.click("css=input.btn.btnC")
                except Exception, err:
                    print Exception, err
                time.sleep(5)
                
                try:
                    sel.click("link=Skip Tagging")
                    sel.wait_for_page_to_load("30000")
                except Exception, err:
                    print Exception, err
                time.sleep(5)

                try:
                    sel.click("css=input.btn.btnC")
                except Exception, err:
                    print Exception, err
                time.sleep(5)

            except Exception, err:
                print Exception, err
                pass
            time.sleep(54*3)
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
