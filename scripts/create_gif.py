__author__ = 'Robert with edits by James'
from images2gif import writeGif
from PIL import Image
import os

file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpeg')))
#['animationframa.png', 'animationframb.png', 'animationframc.png', ...] "
#images = [Image.open(fn) for fn in file_names]
#size = (532,300)
#for im in images:
#	im.thumbnail(size, Image.ANTIALIAS)
#print writeGif.__doc__




i_frame_start = 0
i_frame_end = 9


#print file_names
#print len(file_names)
#exit()

for item in file_names:
	filename = str(i_frame_start)+".GIF"
	these_frames = file_names[i_frame_start:i_frame_end]
	images = [Image.open(fn) for fn in these_frames]
#	print these_frames,images
#	print len(images)
#	exit()
	size = (532,300)
	for im in images:
		im.thumbnail(size, Image.ANTIALIAS)
	if i_frame_end > len(file_names):
		print "i_frame_end greater than number of images"

	writeGif(filename, images, duration=0.17)
	print "attemptcreating "+str(filename)+"\n#####################\n"+str(images)
	i_frame_start = i_frame_end
	i_frame_end = i_frame_start + 9

