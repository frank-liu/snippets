
# adds ttf font to images
# move this to the folder with the resized images
# requires imagemagick mogrify and python
import os

ttfpath = "/usr/share/fonts/truetype/freefont/impact.ttf"

d = os.getcwd()
for filez in os.listdir(d):
    # change gravity to north, northeast, south, west to position font 
    # point size is the size of the font
    # annotate is the pixel position of the text in regards to 0,0
	os.system("mogrify -fill white -font "+ttfpath+" -pointsize 70 -stroke black -strokewidth 2 -gravity north -annotate -4-5 'All projects of \“disillusionment\” for the sake of greater enlightenment:\nsociology is — \nto speak sociologically — \njust a high-culture spokesperson of power.' "+filez)

