from PIL import Image

im = Image.open('tripleten_logo.jpeg')

print(im.size)

rotated = im.rotate(90)

rotated.save('rotated.png')
