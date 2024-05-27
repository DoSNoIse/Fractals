# Mandelbrot fractal
# FB - 201003254
from PIL import Image
import time
# drawing area
xa = -1.227173470375999986752
xb = -1.227171247735999986752
ya = 0.164622890215999999926
yb = 0.164624573071999999926

# max iterations allowed
maxIt = 10000

# image size
imgx = 1000
imgy = 900
image = Image.new("RGB", (imgx, imgy))

start_time = time.time()

for y in range(imgy):
	zy = y * (yb - ya) / (imgy - 1) + ya
	for x in range(imgx):
		zx = x * (xb - xa) / (imgx - 1) + xa
		z = zx + zy * 1j
		c = z
		for i in range(maxIt):
			if abs(z) > 2.0: break
			z = z * z + c
		image.putpixel((x, y), (i % 200*64, i % 80*20, i % 180*64))

end_time = time.time()
time_taken =  end_time - start_time 

final_time = time_taken / (60*60)

print('Execution time:', time_taken,'s', final_time, 'hrs')
image.save('test.png')