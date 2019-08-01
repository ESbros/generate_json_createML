# Scripts en Python para filtrar imagenes(rotacion, brillo, contraste, flip, crop), generar archivos JSON y unir archivos JSON de distintas clases.

## Filtrar Imagenes
#### increase_data.py

Pasar la direccion de la carpeta que contiene las imagenes. (Imagenes formato JPG, JPEG, PNG)


## Crear JSON
#### generate_json.py

Nombre de la imagen: cat_1.jpg, dog_1.png, cat_2.JPEG, dog_2.PNG

Pasar la direccion de la carpeta que contiene las imagenes.

Pasar la direccion donde el archivos JSON se va a guardar.

## Revisen estos links para mas informacion: 
https://medium.com/@eriksols/generate-annotations-json-format-for-createml-apple-with-python-90fc848cd439
https://github.com/ESbros/CreateML_Annotations_JSON


## Unir JSON
#### join_json.py

Pasar la direccion de la carpeta que contiene los archivos JSON de distintas clases.

Pasar la direccion donde el archivo JSON se va a guardar.

#### Ejemplo:
Carpeta con distintos archivos JSON: Dog_Annotation.json, Cat_Annotation.json -> Dog_Cat_Annotation.json


## Iterar JSON
#### open_json.py


# Ceriterios de Busqueda (Imagenes)
Descargar 200 imagenes de cada clase.
Dimension: >1000px(ancho) y >800px (largo)

#### Ejemplo: 
Taxi: Descargar imagenes de taxis en distintas posiciones. Lado, frente, etc.
Perro: Imagenes de perros de distintas razas.
Ropa: Images de prendas sueltas. No vestidas por personas.

