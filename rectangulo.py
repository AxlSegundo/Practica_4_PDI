from PIL import Image, ImageDraw, ImageFilter

# Crea una imagen completamente negra de 4000x3000
imagen = Image.new("RGB", (4000, 3000), "black")

# Crea un objeto ImageDraw para dibujar en la imagen
dibujo = ImageDraw.Draw(imagen)

# Dibuja un rectángulo blanco de 500x700 en la esquina inferior derecha
posicion_rectangulo = (4000 - 1000, 3000 - 600, 4000, 3000)
dibujo.rectangle(posicion_rectangulo, fill="white")

# Aplica un filtro de desenfoque gaussiano al rectángulo
imagen_filtro = imagen.filter(ImageFilter.GaussianBlur(10))

# Guarda la imagen resultante
imagen_filtro.save("IMG/imagen_con_rectangulo.jpg")