import re

f = open('Facebook1.html','r+')
g = open('output.txt','w')
g.close()
g = open('output.txt','a')
a = []

for l in f:
	l.replace(">",">\n")
	a.append(l)

g.close()
f.close()
