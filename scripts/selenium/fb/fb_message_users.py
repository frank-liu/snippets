from selenium import selenium
import unittest, time, re

class fb_message_users(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://m.facebook.com/")
        self.selenium.start()
    
    def test_fb_message_users(self):
        sel = self.selenium
        sel.open("/")
        sel.type("name=email", "james.a.munsch@gmail.com")
        sel.type("name=pass", "Drtisdrt??")
        sel.click("name=login")
        sel.wait_for_page_to_load("30000")
        try:
           sel.open("independentink")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sunita12")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("leroy.a.white.12")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("vincent.roscoe")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("tuula.rebhahn")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("chronicsin")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ss1gohan13")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("BobbyBueno")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("FoodCyclesBikeTour")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("adam.jacobson.33633")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("erica.pollert")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("bmarcil2")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dustin.mohagen")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("snots.buttwax")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("KohdCilver")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("allen.bae")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("james.cox.923519")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ashley.forkey")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("joe.bender.33")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jamiedtyson")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jsohd")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("riedeldrew")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("keihly")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("john.wanninger.56")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jakeseph")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("clake.bolby")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dawnielle.christine")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("107857719236701")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("10151402651798920")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dawn.prentice")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jakerenny.rennaker")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("140497129314917")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("events")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jonCates")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("cynthia.trupka")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("www.facebook.com_002")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("michael.mahlum.52")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("marykinstler")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("allie.shaenanigans")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("al.aamodt.7")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("merlin727")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("eric.syvertson")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("erick.johnson.5832")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("kippg")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jojo.hussanebinladenbushjrthethird")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("shanebr1")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("misty.dawn.948")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("vance.walsh")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("caitlin.cross.9")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("victoria.evert")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("chassy.tauberman")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("tiffany.munsch")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ashlee.eng")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("AuthenticRobinWilliams")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("heydt")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ianaleksanderadams")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("AdamBrownPhotographer")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("shelly.swenson.752")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("Laufoo.Chan")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sheila.carleton")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jamian.julianovillani")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("lauren.a.deland")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("andyspof")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("natasha.gray.56")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("allactivity")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("chrishennen")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jorden.c.hunter")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dustin.switters")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("themajestic.vangerud")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("chelseyjoy")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("Myungsunkim")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("anna.mladnick")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("daniel.blickensderfer.5")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("tsaijung.yang.9")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("punchgut")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("108413969183061")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ChelseyMcQuay")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("a.blacktangerine")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ke.larson")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("info")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jeremy.hackley.5")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sandra.miles.1088")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("null.entry_002")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("thomas.jacobson.5")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("Conjohn13")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("106475742755603")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("elise.forer")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ann.blickensderfer")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("10152698593780694")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("zimmermi")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dwightenheimer")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("michael.pink.98")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("suzi.belanus")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ashley.j.anderson.90")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("browser")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("casey.cables")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("amanda.strauss.94")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("andrew.prassas")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("SupremeGenius")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sidestreet.pub")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jared.shaw.165")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("trennotevenoncebrah")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("david.kelley.3367")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("milind.khandal")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("iam.confus.7")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("codyo3")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("rebecca.munsch")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("blindjoe1")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("michael.w.ramsdell.jr")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("139732189394863")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("amy.e.blickensderfer")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("charles.w.kelm")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("josh.stallard.79")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dinanas")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("aquarium.dempseys")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("theredravenespressoparlor")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("nathan.l.denny")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jgysland")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dylan.leikvoll")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("matt.qual")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("privacy")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("rmoldenhauer1")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("null.entry_003")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("242003382481359")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jennifer.hintz.7")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("michael.daum")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jami.bolduc")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("Justine.Roy4")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ClintKliewer")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sonar.nazarian")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("app_angrybirds")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("nicholas.kory")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("richard.ness.75")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("danielrhuss")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("kevinrbrehmer")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("106469306054854")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("carrie.v.hofmann")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("settings_003")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("brittney.goodman.3")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("MatthewEHoffman")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ads")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("meyersklaus")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("requests")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("cory.yep")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jordan.woroniecki")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sherry.wells.1656")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jared.hernandez.3388")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jodi.niles.3")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("coffeencigarettes")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("joshua.boschee")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("crystal.aaland")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("micah.koosmann")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sabrina.hornung.50")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("chrissy.colbert")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("serena.tibor")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("screamingmechanicalbrain")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("bradley.deelstra")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("courtney.schur.3")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sarahmariesmart")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sarah.deschenes.33")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ted.tyler.12")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("www.facebook.com_004")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sibbsz")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("108090249212525")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("112133132139995")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("help")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("HeyItsMatthew")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dawnielle.gadacz.9")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("seth.warwas")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("stpetecollege")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("luke.schieve")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("michael.jordan.73932")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("msum.arteducators")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("pat.bevans.71")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("anytime.jones")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("debdawsonfargo")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("183092545050814")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("135057883191383")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("peter.splunder")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("mothers.moorhead")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("majestic1026")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("144021142292822")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("TASERGUNFUN")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("bradybaxteronline")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("joel.heitkamp")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("pickled.parrot.1")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dutto30")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("christopher.albee")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("holden.harwood")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("bone.skot")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("tlc.cleaning.5")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("nate.murray.982")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("policies")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("KalamityKristen")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("messages")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("haley.kaspari")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("loviniswhativegot")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("becca.payne.75")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("travis.voss.501")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("justntyme.diva")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("scott.kramlich")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("iampookala")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("cathy.thurston.7")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("102653546485619")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("fargo.police")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("nikki.andersonwait")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("edenparkermusic")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("Daley001")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("toshalynn88")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("amethyst.auditore")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("134756369904710")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("147917451888203")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("157824277712280")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("mike.kvanvig")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("AdamCaptainDelicious")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("emily.l.09")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dean.hadland")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jason.s.sellers.1")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("kshitij.maurya.10")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("albert.rodriguez.330467")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("tay.stevenson1")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("peggy.n.jason")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("james.wolberg.3")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("peter.winch.5")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("brookswest")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("maggie.johnson.96")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("catie14")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("Cirkadian")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("lewis.denny.7")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("kcmac17")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("princessmobydolphinpalmtreechristmastomhankscouch")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("105668726134217")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("thankyougianteagle")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jared.norris.399")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jake.larson.311")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ChuckU612")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("nora.sharpkretzman")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("371369641615")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("103311606393409")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("wrhall")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("natalie.niager")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("cglaserthurston1")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jayinee.basu")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("anthony.belfiori")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("112705862078558")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("smsdslowkid")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("mitch.dokken")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("CGProgram")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("Kaydee")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("nathaniel.leal")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("nathan.dessonville")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("tammy.swift.98")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("robert.dolney")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jaide.morison")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("10152698598795694")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("199351453495899")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("rusty.steele2")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("charles.milas")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("zhimin.guan")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("saic.admissions")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dennis.walaker")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("james.sibelle")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("settings_002")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("ricardo.paniagua.54")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("joseph.schmitz.90")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("105606836140307")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("art.materials.5")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("monica.ohm")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("alyssa1277")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("heidi.heitkamp.33")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("fmfreedomfighters")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("thomas.moriarty.73")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("stacie.schottenbauer")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("david.huttner")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("Bpapes")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("dudley.dexter")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("daywalkerofthemidwest")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("chuck.hues")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("tjmunsch")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jescia.hopper")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jimmythehorn")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("sailor.sammi.7")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("www.facebook.com")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("david.rickards.37")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("justin.whitman1")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("alex.hajicek")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("colebritton2")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("kayla.wixo")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("mark.murphy.505")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("beth.stone.9862")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("kari.selliehanson")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("nick.brutscher.1")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("beau.fraase")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("mackenzie.kouba")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("jamie.shore.963")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)
        try:
           sel.open("app_soundcloud")
           sel.click("link=Message")
           sel.wait_for_page_to_load("3000")
           sel.type("id=composerInput", "you are special. how do we know each other? how did we meet?     If we met for coffee tomorrow, I would show up in a banana costume, what are your thoughts on this situation? your reactions, thoughts, and what would we talk about?")
           sel.click("name=send")
           sel.wait_for_page_to_load("30000")
        except Exception, err:
            print Exception, err
            pass
        time.sleep(24)

    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
