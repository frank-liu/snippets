from selenium import selenium
import unittest, time, re
import time
import os


class fb_post(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4445, "*chrome", "https://")
        self.selenium.start()
    
    def test_fb_post(self):
        sel = self.selenium
        sel.open("www.facebook.com/")
        sel.type("id=email", "james.a.munsch@gmail.com")
        sel.type("id=pass", "Drtisdrt??")
        sel.click("id=u_0_4")
        sel.wait_for_page_to_load("30000")
        sel.open("www.facebook.com/null.entry?ref=tn_tnmn")
        a = []

        for fn in os.listdir("/home/local/Desktop/annoying_banner_ads"):
            a.append("/home/local/Desktop/annoying_banner_ads/"+fn)

        b = []
        f = open("/home/local/Desktop/sex_ad_text","r")
        for l in f:
            b.append(l)

        while True:
            try:
                fn = a.pop(0)
                print fn
                self.post_pic(fn)
            except:
                pass
            try:            
                l = b.pop(0)
                print l
                self.post_txt(l)
            except:
                pass
    def post_txt(self,l):
        sel = self.selenium
        sel.open("www.facebook.com/")
        sel.open("www.facebook.com/null.entry?ref=tn_tnmn")

        try:
            sel.mouse_move("id=u_0_2v")
            sel.click("id=u_0_2v")
            sel.key_down("id=u_0_2v", "\\11")
            sel.key_up("id=u_0_2v", "\\11")
            sel.key_down("id=u_0_2v", "\\11")
            sel.key_up("id=u_0_2v", "\\11")
            sel.key_down("id=u_0_2v", "\\11")
            sel.key_up("id=u_0_2v", "\\11")
            sel.type("id=u_0_2v", l)
            sel.key_down("id=u_0_2v", "\\13")
            sel.key_up("id=u_0_2v", "\\13")
            for i in range(60):
                try:
                    if "Post" == sel.get_text("//button[@value='1']"): break
                except: pass
                time.sleep(1)
            else: fail("time out")
            sel.click("//button[@value='1']")
            time.sleep(60)
            print "text upload attempted"
        except Exception, err:
            print Exception, err
            pass
        time.sleep(60)
        return

    def post_pic(self,fn):
        sel = self.selenium
        try:
            sel.open("m.facebook.com/")
            sel.open("m.facebook.com/?_rdr")
            sel.click("link=More Options")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Upload Photo")
            sel.wait_for_page_to_load("30000")
            sel.type("name=file1", fn)
            sel.click("css=input.btn.btnC")
            sel.wait_for_page_to_load("30000")
            try:
                sel.click("link=Skip Tagging")
                sel.wait_for_page_to_load("30000")
            except Exception, err:
                print Exception, err
                pass

            try:
                sel.click("css=input.btn.btnC")
                sel.wait_for_page_to_load("30000")
            except Exception, err:
                print Exception, err
                pass

        except Exception, err:
            print Exception, err
            pass
        sel.click("css=input.btn.btnC")
        sel.wait_for_page_to_load("30000")
        time.sleep(60)
        return




    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()