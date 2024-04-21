from PIL import Image, ImageChops, ImageFilter, ImageOps

def gaussian_blur(image, radius=2):
    return image.filter(ImageFilter.GaussianBlur(radius))

def merge_images(image1, image2, image3):
    # Aplicar suavizado gaussiano a cada imagen
    blurred_image1 = gaussian_blur(image1)
    blurred_image2 = gaussian_blur(image2)
    blurred_image3 = gaussian_blur(image3)

    # Convertir a modo de operación RGB si no lo está
    if blurred_image1.mode != 'RGB':
        blurred_image1 = blurred_image1.convert('RGB')
    if blurred_image2.mode != 'RGB':
        blurred_image2 = blurred_image2.convert('RGB')
    if blurred_image3.mode != 'RGB':
        blurred_image3 = blurred_image3.convert('RGB')

    # Combinar las imágenes tomando el promedio de los píxeles
    merged_image = Image.blend(blurred_image1, blurred_image2, 1/3)
    merged_image = Image.blend(merged_image, blurred_image3, 1/3)

    return merged_image
def combinar(Objeto,FondoN,Mascara):
    mascara_invertida = ImageOps.invert(Mascara)
    parte_fondo = ImageChops.multiply(FondoN,mascara_invertida)
    parte_objeto = ImageChops.multiply(Objeto,Mascara)
    combinar_imagenes = ImageChops.add(parte_fondo,parte_objeto)
    return combinar_imagenes
# Cargar las tres imágenes
image1 = Image.open("Nueva_prueba/img/Fondo1.jpg")
image2 = image1
image3 = image1

# Combinar las imágenes utilizando suavizado gaussiano
merged_image = merge_images(image1, image2, image3)
merged_image.save("Nueva_prueba/img/merged_image.jpg")

# Guardar la imagen combinada
Modelo = Image.open("Nueva_prueba/img/merged_image.jpg")
Objeto = Image.open("Nueva_prueba/img/objetoN.jpg")
Fondo_nuevo = Image.open("Nueva_prueba/img/Fondo_nuevo.jpg")

diferencia_absoluta = ImageChops.difference(Modelo,Objeto)
diferencia_absoluta.convert("L")
umbral=37
mascara_bin = diferencia_absoluta.point(lambda p: 255 if p > umbral else 0)
mascara_bin = mascara_bin.filter(ImageFilter.MinFilter(3))
mascara_bin = mascara_bin.filter(ImageFilter.MaxFilter(5))



imagen_f=combinar(Objeto,Fondo_nuevo,mascara_bin)
imagen_f.show()
