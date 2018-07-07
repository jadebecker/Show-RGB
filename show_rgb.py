import PIL
from PIL import Image
from PIL import ImageOps
import sys

if len(sys.argv) > 1:
	img = sys.argv[1]


image = Image.open(img).convert("RGB")
chan = image.split()

red = chan[0]
red = ImageOps.colorize(red,(255,255,255),(255,0,0))
red.show()
green = chan[1]
green = ImageOps.colorize(green,(255,255,255),(0,255,0))
green.show()
blue = chan[2]
blue = ImageOps.colorize(blue,(255,255,255),(0,0,255))
blue.show()

