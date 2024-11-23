import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np


class Nodo:
    def __init__(self, label, score):
        self.label = label
        self.score = score
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, label, score):
        nuevo_nodo = Nodo(label, score)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        i = 1
        while actual:
            print(f"{i}. {actual.label}: {actual.score:.2f}")
            actual = actual.siguiente
            i += 1


model = MobileNetV2(weights='imagenet')


img_path = '/content/descarga (2).jpg'  

img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)


predictions = model.predict(img_array)


decoded_predictions = decode_predictions(predictions, top=3)[0]
lista_predicciones = ListaEnlazada()

for imagenet_id, label, score in decoded_predictions:
    lista_predicciones.agregar(label, score)


print("Predicciones:")
lista_predicciones.imprimir_lista()