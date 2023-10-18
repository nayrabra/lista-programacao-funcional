from PIL import Image

image_path = '/Users/nayrabraga/Desktop/adsS3/Programação Funcional/av2Python/AV2_NayraBarbosa/gatinho.jpeg'
img = Image.open(image_path)

width, height = img.size

modify_pixel = lambda pixel: tuple(map(lambda x: min(255, x + 30), pixel))

for x in range(width):
    for y in range(height):
        original_pixel = img.getpixel((x, y))
        modified_pixel = modify_pixel(original_pixel)
        img.putpixel((x, y), modified_pixel)

print("Antes: ", img.getpixel((0, 0)))
print("Depois: ", modify_pixel(img.getpixel((0, 0))))

img.save('/Users/nayrabraga/Desktop/adsS3/Programação Funcional/av2Python/AV2_NayraBarbosa/gatinho_modificado.jpeg')
