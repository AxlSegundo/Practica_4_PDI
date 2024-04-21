from PIL import Image, ImageChops, ImageOps
Fondo_nuevo = Image.open("img/NuevoFondo.jpg")
rectangulo_nombre = Image.open("img/imagen_con_rectangulo_nombre.jpg")
rectangulo = Image.open("img/imagen_con_rectangulo.jpg")
rectangulo.convert("L")
umbral = 80
rectangulo = rectangulo.point(lambda p:255 if p > umbral else 0 )
rectangulo_invertido = ImageOps.invert(rectangulo)
F_y_R= ImageChops.multiply(Fondo_nuevo.convert("RGB"),rectangulo_invertido.convert("RGB"))
N_y_R = ImageChops.multiply(rectangulo_nombre.convert("RGB"),rectangulo.convert("RGB"))
Nuevo_fondo = ImageChops.add(F_y_R,N_y_R)
Nuevo_fondo.save("IMG/Fondo_nuevo.jpg")