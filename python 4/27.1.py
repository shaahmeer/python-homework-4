from PIL import Image


def make_preview(size, n_colors):
    img = Image.open('27.1.jpg')
    img = img.resize(size)
    img = img.quantize(colors=n_colors)
    img.save('27.1.bmp', 'BMP')


make_preview((200, 150), 10)
