from selenium import selenium
import unittest, time, re

class temp(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4447, "*chrome", "http://")
        self.selenium.start()
    
    def test_temp(self):
        sel = self.selenium
        sel.open("tumblr.com/login")
        sel.type("id=signup_email","james.a.munsch@gmail.com")
        sel.type("id=signup_password", "Drtisdrt??")
        sel.click("id=signup_forms_submit")
        sel.wait_for_page_to_load("30000")
        time.sleep(11)

        try:
            sel.open("ruineshumaines.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("ruineshumaines.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("jeffdtaylor.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("jeffdtaylor.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("champagneproblems.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("champagneproblems.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("showslow.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("showslow.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("blog.jacobvanloon.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("blog.jacobvanloon.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("arpeggia.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("arpeggia.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("tylervarsell.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("tylervarsell.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("blackcontemporaryart.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("blackcontemporaryart.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("artsatlas.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("artsatlas.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("rery.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("rery.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("futureshipwreck.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("futureshipwreck.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("jenna.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("jenna.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("atavus.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("atavus.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("ryandonato.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("ryandonato.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("anniewerner.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("anniewerner.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("www.cavetocanvas.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("www.cavetocanvas.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("www.valentineuhovski.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("www.valentineuhovski.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("anniewerner.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("anniewerner.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("exhibition-ism.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("exhibition-ism.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("thisbelongsinamuseum.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("thisbelongsinamuseum.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("anniewerner.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("anniewerner.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("tumblropenarts.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("tumblropenarts.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("creativetime.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("creativetime.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("artruby.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("artruby.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("devidsketchbook.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("devidsketchbook.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("deadrabbitohno.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("deadrabbitohno.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("slowartday.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("slowartday.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("likeafieldmouse.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("likeafieldmouse.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("blue-voids.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("blue-voids.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("darksilenceinsuburbia.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("darksilenceinsuburbia.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("artchipel.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("artchipel.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("yama-bato.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("yama-bato.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("visual-poetry.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("visual-poetry.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("areaofinterest.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("areaofinterest.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("theartofanimation.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("theartofanimation.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("frenchtwist.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("frenchtwist.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
            sel.open("samanthakeelysmith.tumblr.com/")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Follow")
       #     sel.open("samanthakeelysmith.tumblr.com/ask")

        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)

    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
