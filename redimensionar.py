from PIL import Image

# Abre la imagen
imagen = Image.open("IMG\Piramide_Or.jpg")

# Redimensiona la imagen a 4000 x 3000 píxeles
imagen_redimensionada = imagen.resize((4000, 3000))

# Guarda la imagen redimensionada
imagen_redimensionada.save("IMG/Piramide_Red.jpg")
