from PIL import Image


def image_filter(pixels, i, j):
    if pixels[i][j] > 0:
        pixels[i][j] -= 2
    return pixels[i][j]


img = Image.open('27.1.bmp')
width, height = img.size
pixels = [list(img.getdata())[n:n+width] for n in range(0, width*height, width)]
for i in range(width):
    for j in range(height):
        img.putpixel((i, j), image_filter(pixels, j, i))
img.save('27.2.png', 'PNG')
