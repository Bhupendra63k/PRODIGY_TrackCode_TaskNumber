
with open("C:/Users/naray/Downloads/WhatsApp Image 2024-02-20 at 21.15.56.jpeg", "rb") as file:
    image = file.read()

image = bytearray(image)
key = 20

for v, j in enumerate(image):
    image[v] = j ^ key

with open("encrypted.jpg", "wb") as file:
    file.write(image)
    file.close()
