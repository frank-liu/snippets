import re
from collections import OrderedDict



#################################################3
# FORMAT facebook output html
#########################################################

f = open('Facebook1.html','r+')
g = open('output.txt','w')
g.write("")
g.close()
g = open('output.txt','a')
a = []

h = open('output.txt','r+')
i = open('post_pages.txt','w')
i.write("")
i.close()
i = open('post_pages.txt','a')
b = []


for l in f:
	z = l.replace(">",">\n")
	zz = z.replace(" ","")
	zzz = zz.replace("\n\n","\n")
	zzzz = zzz.replace("\n\n","\n")
	zzzzz = zzzz.replace("\n\n","\n")
	a.append(zz)

for item in a:
	g.write(item)
g.close()
i.close()

###################################################################
# split lines in output.txt
##################################################################


f = open("output.txt","r")
a = []

for l in f:
	if "<ahref=\"https://www.facebook.com/" in l:
		y = l.split("\"")
		for item in y:
			if "posts" in item:
				a.append(item)

b = []
for item in a:
	if "?" in item:
		continue
	z = item.replace("<ahref=\"https://www.facebook.com/","")
	b.append(z)	

this = OrderedDict.fromkeys(b).keys()








#########################################################
#
#
##########################################################


g = open("likes.txt","w")
g.write("")
g = open("likes.txt","a")

for items in this:
	items = items.replace("https://www.facebook.com/","")
	g.write("        try:\n")
	g.write("            for i in range(30):\n")
	g.write("                try:\n")
	g.write("                    if sel.is_text_present(\"Like\"): break\n")
	g.write("                except: pass\n")
	g.write("                time.sleep(1)\n")
	g.write("            else: self.fail(\"time out\")\n")
	g.write("            sel.open(\""+items+"\")\n")
	g.write("            sel.mouse_move(\"id=.reactRoot[0]\")\n")
	g.write("            sel.click(\"id=.reactRoot[0]\")\n")
	g.write("            time.sleep(5)\n")
	g.write("        except Exception, err:\n")
	g.write("            print Exception, err\n")
	g.write("            pass\n")
g.close()
f.close()


