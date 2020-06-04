

import pygame
from PIL import Image
width, height = 1000,1000
screen = pygame.display.set_mode((width, height))
img=Image.new("RGB",(width,height))
xaxis = width / 1.5 + 140
yaxis = height / 2
scale = 400
maxit = 99
for iy in range(int(height/2)+1):
    for ix in range(width):
        z = 0 + 0j

        c = complex(float(ix - xaxis) / scale, float(iy - yaxis) / scale)

        for it in range(maxit):
            z = z*z + c
            if abs(z) > 2:
                col=(it % 4 * 64, it % 8 * 32, it % 16 * 16)
                break
        else:
            col = (0, 0, 0)

        screen.set_at((ix, iy), col)
        screen.set_at((ix, height-iy), col)
        img.putpixel((ix,iy),col)
        img.putpixel((ix,height-iy-1),col)
    pygame.display.update()
raw_input("Done")
img.save("Mandelbrot.png", "PNG")