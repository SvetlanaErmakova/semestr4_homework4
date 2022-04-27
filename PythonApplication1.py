import numpy as np
from PIL import Image

if __name__ == '__main__':
    try:
        im1= Image.open('im1.jpg')
        im2= Image.open('im2.jpg')
    except OSError:
        print("error: cant open image")
        exit()

    (w1,h1)= im1.size
    (w2,h2)= im2.size
    if(w1<w2 or h1<h2):
        print("error: size1 must be bigger size2")
        exit()
    rez_im = im1.copy()
    rez_im.paste(im2, (int(w1/2-w2/2), int(h1/2-h2/2)))
    rez_im.save('im_rez.jpg', quality=95)
 
    im1.close()
    im2.close()
