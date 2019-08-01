# Scripts en Python para filtrar imagenes(rotacion, brillo, contraste, flip, crop), generar archivos JSON y unir archivos JSON de distintas clases.

## Filtrar Imagenes
#### increase_data.py

Pasar la direccion de la carpeta que contiene las imagenes. (Imagenes formato JPG, JPEG, PNG)


## Crear JSON
#### generate_json.py

Nombre de la imagen: cat_1.jpg, dog_1.png, cat_2.JPEG, dog_2.PNG

Pasar la direccion de la carpeta que contiene las imagenes.

Pasar la direccion donde el archivos JSON se va a guardar.

## Revisen este link para mas informacion: 
https://medium.com/@eriksols/generate-annotations-json-format-for-createml-apple-with-python-90fc848cd439


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


## Distribucion 
Elias: 1 - 68 primeras clases
Santiago: 69 - 136  
Bryan Eduardo: 137 - 204
Marcos Fernando: 205 - 272
Genesis: 273 - 340
Marcos: 341
Bryan: 342

# Importante
Deben tener 200 imagenes por cada clase, pero no es necesario descargar las 200 imagenes crudas. Sino por ejemplo: 50 imagenes crudas y aplicar 4 filtros a cada imagen(Aumentar-Disminuir brillo/contraste, crop, flip). Lo que en total les daria 200 imagenes en total. No recomendable aplicar a todas las clases filtros de rotacion, por ejemplo para autos no seria conveniente pero si lo seria para ropa, etc. 
