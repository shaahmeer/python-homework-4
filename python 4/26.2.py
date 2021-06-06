from PIL import Image, ImageDraw


def board(n, size):
    img = Image.new('RGB', (n*size, n*size))
    draw = ImageDraw.Draw(img)
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                color = (0, 0, 0)
            else:
                color = (255, 255, 255)
            x, y = i * size, j * size
            draw.rectangle((x, y, x + size, y + size), fill=color)
    img.save('26.2.png', 'PNG')


board(8, 50)
