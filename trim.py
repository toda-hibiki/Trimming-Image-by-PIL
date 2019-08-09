from PIL import Image

im = Image.open('vessel1-1.eps')

#im_crop = im.crop((0,1024,512,1536))
im_crop = im.crop((0,512,0,512))
im_crop.save('670_suda.png', quality=95)
