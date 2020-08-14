import cv2 as cv
import imageio
import os
from utils import agregar_imagen

script_dir = os.path.dirname(os.path.realpath(__file__))
image_dir = os.path.join(script_dir, 'imagenes')

pa = {
    'x': 20, 'y': 20,
    'w': 250, 'h': 250
}

cerveza = imageio.imread(os.path.join(image_dir,"cerveza.jpg"))
mascara = imageio.imread(os.path.join(image_dir,"stormtrooper-ojos-transparentes.png"))
mascara_chico = cv.resize(mascara, (pa['w'], pa['h']) ) 
print(mascara.shape)

agregar_imagen(cerveza, mascara, 200, 200)
cv.imshow('Ttulo de la ventana', cerveza)
	
# capturar imagen desde la webcam
cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read() # leer la webcam
    img = cv.flip( img, 1 ) # flip horizontal para que sea un espejo
    
    agregar_imagen(img, mascara_chico, 200, 200)

    cv.imshow('Ttulo de la ventana', img)

    k = cv.waitKey(30)
    if k == 27: # ESC (ASCII)
        break
cap.release()
cv.destroyAllWindows()