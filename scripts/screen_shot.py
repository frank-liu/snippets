import gtk
import PIL
from PIL import Image
from time import gmtime, strftime
import time

def s():
 try:

   img_width = gtk.gdk.screen_width()
   img_height = gtk.gdk.screen_height()

   screengrab = gtk.gdk.Pixbuf(
     gtk.gdk.COLORSPACE_RGB,
     False,
     8,
     img_width,
     img_height
   )

   screengrab.get_from_drawable(
     gtk.gdk.get_default_root_window(),
     gtk.gdk.colormap_get_system(),
     0, 0, 0, 0,
     img_width,
     img_height
   )

 except:
    print "Failed taking screenshot"
    exit()

 print "Converting to PIL image ..."

 final_screengrab = Image.frombuffer(
   "RGB",
   (img_width, img_height),
   screengrab.get_pixels(),
   "raw",
   "RGB",
   screengrab.get_rowstride(),
   1
 )

 final_screengrab.save("/home/local/Desktop/scripts/"+strftime("%H-%M-%S"),"JPEG")

max_time = 3*60*60
start_time = time.time()  # remember when we started
while (time.time() - start_time) < max_time:
	s()
	time.sleep(1)


