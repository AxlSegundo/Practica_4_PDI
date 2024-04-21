from PIL import Image, ImageDraw

# Crea una imagen completamente negra de 4000x3000
imagen = Image.new("RGB", (4000, 3000), "black")

# Crea un objeto ImageDraw para dibujar en la imagen
dibujo = ImageDraw.Draw(imagen)

# Dibuja un rectángulo blanco de 1000x600 en la esquina inferior derecha
posicion_rectangulo = [(4000 - 1000, 3000 - 600), (4000, 3000)]
dibujo.rectangle(posicion_rectangulo, fill="white")

# Guarda la imagen resultante
imagen.save("IMG/imagen_con_rectangulo_nombre.jpg")