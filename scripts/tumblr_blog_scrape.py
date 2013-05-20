import re
import time
from urllib import FancyURLopener
import urllib2

class MyOpener(FancyURLopener): 
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
myopener = MyOpener()




number = 365461437

while number > 0:
    url = "http://www.tumblr.com/tagged/contemporary?before=1"+str(number)
    g = open(str(number)+".html","w")
    page = myopener.retrieve(url,str(number)+".html")

    number = number - 5700
    time.sleep(1)


