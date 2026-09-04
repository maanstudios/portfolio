from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

im = Image.open('assets/ZoomCall.png')
# Since it might not be perfectly uniform, let's just use getbbox on the image itself if the background is black/transparent
# or find the bounding box of non-black pixels.
im = im.convert("RGBA")
# black is (0,0,0) to maybe (30,30,30). 
# But Zoom window might have a grey border. 
