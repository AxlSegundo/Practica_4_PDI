from PIL import Image, ImageChops, ImageFilter, ImageOps
#   Se genera un suaviazdo con el fin de obtener un mejor resultado
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
    #   NOT U (invertimos la mascara(U))
    mascara_invertida = ImageOps.invert(Mascara)
    #   F AND NOT U -> (combinamos el fondo nuevo(F) y la mascara invertida(NOT u))
    parte_fondo = ImageChops.multiply(FondoN,mascara_invertida)
    #   A AND U -> (combinamos la imagen donde aparece el objeto a "cortar" y la mascara (U))
    parte_objeto = ImageChops.multiply(Objeto,Mascara)
    #   R= (F AND NOT U) OR (A AND U) -> (Combinamos los procesos anteriores)
    combinar_imagenes = ImageChops.add(parte_fondo,parte_objeto)
    return combinar_imagenes
# Cargar las tres imágenes
image1 = Image.open("IMG/Fondo1.jpg")
image2 = Image.open("IMG/Fondo2.jpg")
image3 = Image.open("IMG/Fondo3.jpg")

#   Combinar las imágenes utilizando suavizado gaussiano
merged_image = merge_images(image1, image2, image3)
#   Guardar la imagen combinada
merged_image.save("IMG/merged_image.jpg")
#   Abrimos las imagenes necesarias para la combinación
Modelo = Image.open("IMG/merged_image.jpg")
Objeto = Image.open("IMG/objetoN.jpg")
Fondo_nuevo = Image.open("IMG/Piramide_Red.jpg")
#   Obtenemos la diferencia entre el modelo y el objeto que queremos segmentar
diferencia_absoluta = ImageChops.difference(Modelo,Objeto)
#   Para poder tener mejor resultado convertimos a escala de grises
diferencia_absoluta.convert("L")
#   Aplicamos un umbral para tener mejor precisión
umbral=37
#   Obtenemos la mascara binaria que nos ayudara en la combinación de imagenes
mascara_bin = diferencia_absoluta.point(lambda p: 255 if p > umbral else 0)
mascara_bin = mascara_bin.filter(ImageFilter.MinFilter(3))
mascara_bin = mascara_bin.filter(ImageFilter.MaxFilter(5))
#   Llamamos a la función encargada de unir las imagenes
imagen_f=combinar(Objeto,Fondo_nuevo,mascara_bin)
#   Mostramos el resultado
imagen_f.save("IMG/imagen_comb.jpg")
imagen_f.show()
