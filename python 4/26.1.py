from PIL import Image, ImageDraw


def gradient(color):
    colors = {"R": 0, "G": 0, "B": 0, color: 1}
    new_image = Image.new('RGB', (512, 200))
    draw = ImageDraw.Draw(new_image)
    for i in range(0, 512, 2):
        c = (colors["R"] * i//2, colors["G"] * i//2, colors["B"] * i//2)
        draw.line((i, 0, i, 200), fill=c, width=1)
        draw.line((i + 1, 0, i + 1, 200), fill=c, width=1)
    new_image.save('26.1.png', 'PNG')


gradient('R')
