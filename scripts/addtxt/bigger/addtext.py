#!/usr/bin/python
#coding: utf-8
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


	os.system("mogrify -fill white -font "+ttfpath+" -pointsize 80 -stroke black -strokewidth 2 -gravity north -annotate -4-5 'All projects of \n\"disillusionment\"for the sake of\ngreater enlightenment:' "+filez)
	os.system("mogrify -fill white -font "+ttfpath+" -pointsize 80 -stroke black -strokewidth 2 -gravity south -annotate -4-5 '\nsociology is -to speak \nsociologically-\njust a high-culture\nspokesperson of power.' "+filez)
    
