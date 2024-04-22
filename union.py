from PIL import Image, ImageChops, ImageOps
#   Abrimos las imagenes para combinar
Fondo_nuevo = Image.open("IMG/imagen_comb.jpg")
rectangulo_nombre = Image.open("IMG/imagen_con_rectangulo_nombre.jpg")
rectangulo = Image.open("IMG/imagen_con_rectangulo.jpg")
rectangulo.convert("L")
#   Con el umbral buscamos mejorar la precisión al momento de juntar
umbral = 80
rectangulo = rectangulo.point(lambda p:255 if p > umbral else 0 )
rectangulo_invertido = ImageOps.invert(rectangulo)
#   F AND NOT R -> Combinamos el Fondo con el rectangulo invertido
F_y_R= ImageChops.multiply(Fondo_nuevo.convert("RGB"),rectangulo_invertido.convert("RGB"))
#   N AND R -> Combinamos el rectangulo con nombre y difuminado, con el rectangulo normal
N_y_R = ImageChops.multiply(rectangulo_nombre.convert("RGB"),rectangulo.convert("RGB"))
#   (F AND NOT R) OR (N AND R) -> Juntamos los dos procesos
Nuevo_fondo = ImageChops.add(F_y_R,N_y_R)
# Guardamos la foto que nos ayudara con el proceso principal
Nuevo_fondo.save("IMG/Fondo_nuevo.jpg")
Nuevo_fondo.show()