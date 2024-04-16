from PIL import Image
import time
from numba import njit
xa = -1.368042451651643662961
xb = -1.364854090282074117281       # This is crazybrot...
ya = 0.017631233174068730298        # do 1000 It and 10000 x 9000 px
yb = 0.019424686444451599818

# max iterations allowed
maxIt = 1000

# image size
imgx = 10000
imgy = 10000
image = Image.new("RGB", (imgx, imgy))

@njit
def func():
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = zx + zy * 1j
            c = z
            for i in range(maxIt):
                if abs(z) > 2.0:
                    break
                z = z * z + c
                image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))

