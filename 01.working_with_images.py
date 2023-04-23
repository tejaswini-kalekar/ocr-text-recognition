from PIL import Image
im_file = "data/Certificate.png"
im = Image.open(im_file)
print(im)
print(im.size)
im.show()
im.save("temp/Certificate.png")
