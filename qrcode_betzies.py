import qrcode

url = "https://leonfallair.github.io/Betzies/"

img = qrcode.make(url)
img.save("qrcode.png")
img.show()