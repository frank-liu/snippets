#
# resizes the images in current folder
#
import os
d = os.getcwd()



for f in os.listdir(d):
    if f.endswith(".png"):
        print f
        g = f.replace(" ","_")
        g = g.replace(":","")
        os.rename(f,g)
    print "#################### do convert"
    os.system("convert "+str(f)+" -resize 1200x1200 "+"bigger"+f)
    print "#################### convert results ^^^^^^^^^^"
    try:
        os.mkdir('bigger')
    except:
        pass
    try:
        os.system('mv bigger* ./bigger')
    except:
        pass

print "### done"

#os.system("cp addtext.py ./bigger")
#print "### cp addtext"
