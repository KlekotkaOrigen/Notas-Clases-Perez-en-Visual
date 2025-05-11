# %% [markdown]
# ## Trabajo Práctico – Clases y Objetos

# %% [markdown]
# 1) Realizar un programa para calcular el monto total a pagar por cada mesa en un restaurante. Realizar el programa usando objetos para almacenar la información de los pedidos de cada mesa y calcular el importe total a pagar. ¿Qué estructura de datos necesita para almacenar la información?

# %%
from tkinter import messagebox

class Pedido:
    def __init__(self, numero_mesa: int, codigo_item: list, costo: float = 0) -> None:
        self.numero_mesa = numero_mesa
        self.codigo_item = codigo_item
        self.costo = costo

    def calcular_precio(self, menu: list):
        costo = 0
        for valor_individual in self.codigo_item:
            costo += menu[valor_individual]["precio"]
        self.costo = costo
        return costo

########################################################################
# Menu del local
menu = [
    {"codigo": 0, "descripcion": "🍕Pizza jamon y morron", "precio": 9000},
    {"codigo": 1, "descripcion": "🥘Milanesa con fritas", "precio": 8000},
    {"codigo": 2, "descripcion": "🥗Ensalada Caesar", "precio": 6000},
    {"codigo": 3, "descripcion": "🥟Empanadas (3 unidades)", "precio": 5000},
    {"codigo": 4, "descripcion": "🍮Flan con dulce", "precio": 5000},
    {"codigo": 5, "descripcion": "🍼Agua mineral", "precio": 2000},
    {"codigo": 6, "descripcion": "🥤Coca-Cola 500ml", "precio": 3000}
]
# Muestro un desplegable con las opciones a elegir
messagebox.showinfo(
    message="-Pizza jamon y morron $ 9000\n -Milanesa con fritas $ 8000\n - Ensalada Caesar $ 6000\n - Empanadas (3 unidades) $ 5000\n - Flan con dulce $ 5000\n - Agua mineral $ 2000\n - Coca-Cola 500ml $ 3000", 
    title="Restaurante Jäguermaister")

# El camarero establece cuantas mesas hay:
cantidad_mesas = int(input('¿Cuantas cantidad de mesas va a atender?'))

# Pregunto cliente lo que quiere:
pedidos_por_mesa = []
numero_mesa = 0
costo_total = 0

while cantidad_mesas != 0:
    pedido_parcial = [] # Lista que guarda los códigos de cada menú
    quiere_pedir = input('Biendenido al Restaurante Jäguermaister, usted desea pedir')
    cantidad_mesas -= 1
    while quiere_pedir.lower() in ['s','si','y','ye','yes']:
        plato_principal = input('Por favor indique un plato principal')
        if 'piz' in plato_principal.lower():
            pedido_parcial.append(menu[0].get('codigo'))
        elif 'mil' in plato_principal.lower():
            pedido_parcial.append(menu[1].get('codigo'))
        elif 'ens' in plato_principal.lower():
            pedido_parcial.append(menu[2].get('codigo'))
        elif 'emp' in plato_principal.lower():
            pedido_parcial.append(menu[3].get('codigo'))

        bebida = input('Por favor indique una bebida')
        if 'agu' in bebida.lower():
            pedido_parcial.append(menu[5].get('codigo'))
        elif 'coc' in bebida.lower():
            pedido_parcial.append(menu[6].get('codigo'))

        postre = input('Por favor indique un postre')
        if 'fla' in postre.lower():
            pedido_parcial.append(menu[4].get('codigo'))
    
        quiere_pedir = input('¿Quiere pedir algo mas?')

    numero_mesa += 1
    pedido = Pedido(numero_mesa, pedido_parcial) # Guardo el pedido correspondiente a la mesa X
    pedido.calcular_precio(menu)
    pedidos_por_mesa.append(pedido)
    costo_total += pedido.costo

# print(pedidos_por_mesa) # Muestra como se ve el objeto internamente, solo para uso didáctico

# Mostrar los pedidos y el costo total
for pedido in pedidos_por_mesa:
    codigo_a_nombre = []
    for codigo_menu in pedido.codigo_item:
        codigo_a_nombre.append(menu[codigo_menu].get("descripcion"))
    print(f"\nMesa {pedido.numero_mesa}:\n Pedido: {', '.join(codigo_a_nombre)}\n Total: ${pedido.costo}\n")

print(f"\nEl costo total del pedido es de ${costo_total}🍝")

# %% [markdown]
# 2) Realizar un programa que ayude al pintor a realizar el presupuesto. El programa debe calcular la superficie total a pintar y la cantidad de litros de pintura, de una cantidad indeterminada de habitaciones. Cada pared puede tener una abertura (puertas, ventanas, etc.), o no tener ninguna abertura. Las aberturas no se pintan, restar su superficie de las paredes a pintar.
# ¿Qué estructura de datos necesita para almacenar la información?
# Realizar el programa usando objetos para almacenar la información de las habitaciones. Está prohibido el uso de las instrucciones print() e input() dentro de las clases (capricho del profesor).

# %%
class Habitaciones:
    def __init__(self, superficie: int, nombre_habitacion: str) -> None:
        self.superficie = superficie
        self.nombre_habitacion = nombre_habitacion

    def sup_pared(self, alto: float, largo: float):
        return alto * largo

    def sup_abertura(self, alto: float, largo: float):
        return alto * largo
    
    def cantidad_pintura(self, superficie: float, rendimiento: int, manos: int):
        total_pintura = (superficie/rendimiento) * 1.10 * manos
        return total_pintura
    
    def superficie_total(habitaciones: list):
        superficie_total = 0
        for superficies in habitaciones:
            superficie_total += habitacion.superficie
        return superficie_total

##################################################################################
# Inicio lista habitaciones
habitaciones = []

# Inicio la carga preguntando si quiere agregar una habitacion
agregar_habitacion = input('¿Quiere agregar habitación?')

while agregar_habitacion.lower() in ['s','si','y','ye','yes']:
    
    superficie_total = 0
    # Nombro la Habitacion con la que trabajo
    nombre_habitacion = input('¿Que nombre desea asignarle a la habitacion?')

    # Agrego pared, calculo superficie y sumo a superficie total de la habitacion trabajada
    agregar_pared = input('¿Quiere agregar pared?')

    while agregar_pared.lower() in ['s','si','y','ye','yes']:
        
        alto = float(input('Indique el alto de la pared'))
        largo = float(input('Indique el largo de la pared'))
        superficie_total += Habitaciones(0, nombre_habitacion).sup_pared(alto, largo)
        agregar_pared = input('¿Quiere agregar otra pared?')

    # Agrego abertura, calculo superficie y resto a superficie total de la habitacion trabajada
    agregar_abertura = input('¿Quiere agregar una abertura?')

    while agregar_abertura.lower() in ['s','si','y','ye','yes']:
        
        alto = float(input('Indique el alto de la abertura'))
        largo = float(input('Indique el largo de la abertura'))
        superficie_total -= Habitaciones(0, nombre_habitacion).sup_abertura(alto, largo)
        agregar_abertura = input('¿Quiere agregar abertura?')

    # Calculo la pintura para cada habitacion
    rendimiento = int(input('¿Cuál es el rendimiento de su pintura?'))
    manos = int(input('¿Cuántas manos de pintura le va a dar?'))

    habitacion = Habitaciones(superficie_total, nombre_habitacion)
    total_pintura = habitacion.cantidad_pintura(superficie_total, rendimiento, manos)

    print(f'\n🏡La superficie total de la habitación {habitacion.nombre_habitacion} es {habitacion.superficie:.2f}\n, para el cual usted va a necesitar un total de {total_pintura:.2f} litros🧹')
    
    habitaciones.append(Habitaciones(habitacion.superficie,nombre_habitacion))
    
    agregar_habitacion = input('¿Quiere agregar habitación?')

total_a_pintar = Habitaciones.superficie_total(habitaciones)
print(f'\nEl total de superficie a pintar de toda la casa es: {total_a_pintar:.2f} m2 🏘')

# %% [markdown]
# 3) Realizar el programa usando objetos. Está prohibido el uso de las instrucciones print() e input() dentro de las clases (capricho del profesor).
# El programa debe permitir:
# - A) Cargar países, almacenando el nombre, el nombre de su capital y su población.
# - B) Cargar los países limítrofes a un país ya cargado. Los países limítrofes deben ser objetos ya creados en el punto A. Cuando al país A, se le carga el país limítrofe B, automáticamente se cargue en el país B, el país limítrofe A. Es decir, si a Argentina le cargamos el país limítrofe Uruguay, automáticamente se debe cargar a Uruguay el país limítrofe Argentina.
# - D) El usuario selecciona un país, y el programa muestra todos sus países limítrofes.
# ¿Qué estructura de datos necesita para almacenar la información? ¿Cuántas clases son necesarias? ¿Cómo codificar la información?

# %%
class Pais: # Creo el objeto pais con los atributos iniciales para rellenarlos con la lista
    def __init__(self, nombre: str, capital: str, poblacion: int) -> None:
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.limitrofes = []
        
    def agregar_limitrofe(self, otro_pais):
        if otro_pais is not None and otro_pais not in self.limitrofes:
            self.limitrofes.append(otro_pais)
            if self not in otro_pais.limitrofes:
                otro_pais.limitrofes.append(self)

######################################################################################################

lista_objetos_pais = []

# PUNTO A = Carga de paises por parte del usuario

cantidad_paises = int(input('¿Cuantos paises quiere agregar?'))
while cantidad_paises != 0:

    nombre = input('Ingrese nombre del país')
    capital = input('Ingrese capital del país')
    poblacion = int(input('Ingrese la población del pais'))
    
    lista_objetos_pais.append(Pais(nombre, capital, poblacion))
    
    cantidad_paises -= 1

# PUNTO B = Carga paises de paises limitrofes:
pais_a_limitar = input('Indique el nombre del país al que le va a cargar los limítrofes')

for pais_busqueda in lista_objetos_pais : 
    if pais_busqueda.nombre.lower() == pais_a_limitar.lower(): # Busco en lista de objeto PAIS si esta el pais_a_limitar
        
        cantidad_limitrofes = int(input('¿Cuantos paises limítrofes quiere agregar?')) # Si esta pregunto cuantos limitrofes quiero agregar
        while cantidad_limitrofes != 0:
            nuevo_limitrofe = input('Indique el nombre del país vecino')  # Indico el nuevo limitrofe

            # Busco el objeto Pais que coincide con el nombre del nuevo_limitrofe
            obj_limitrofe = None
            for pais in lista_objetos_pais:
                if pais.nombre.lower() == nuevo_limitrofe.lower():
                    obj_limitrofe = pais
                    break

            # Si lo encontré, lo agrego con el método que también lo hace mutuo
            if obj_limitrofe is not None:
                pais_busqueda.agregar_limitrofe(obj_limitrofe)

            cantidad_limitrofes -= 1

# PUNTO C = El usuario indica que país quiere elegir
seleccion = input("¿Qué pais quiere elegir?")

for busqueda in lista_objetos_pais:
    if busqueda.nombre.lower() == seleccion.lower():
        print(f'🗺 Su pais elegido es: {seleccion}\n Y los limitrofes de {seleccion} son: {[pais.nombre for pais in busqueda.limitrofes]}')

# %%
# Versión sin acceder a la API

from tkinter import messagebox

class Paises: # Creo el objeto pais con los atributos iniciales para rellenarlos con la lista
    def __init__(self, nombre: str, capital: str, poblacion: int, limitrofes) -> None:
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.limitrofes = limitrofes

    def obtener_paises(diccionario): # Con self no me funcionaba - Guarda las instancias de la lista predefinida
        lista_paises = []
        for i in diccionario:
            nombre = i["nombre"]
            capital = i["capital"]
            poblacion = i["poblacion"]
            limitrofes = []
            pais = Paises(nombre,capital,poblacion, limitrofes)
            lista_paises.append(pais)
        return lista_paises

    def construccion_limitrofes(lista_paises_objeto, lista_original):
        for pais_objeto in lista_paises_objeto:
            # Buscamos el diccionario original que coincide con este país
            for pais_dic in lista_original:
                if pais_dic["nombre"] == pais_objeto.nombre:
                    # Si encontramos el país, trabajamos con su lista de limítrofes
                    for nombre_vecino in pais_dic["limitrofes"]:
                        for posible_vecino in lista_paises_objeto:
                            if posible_vecino.nombre == nombre_vecino:
                                # Nos aseguramos que no esté repetido
                                if posible_vecino not in pais_objeto.limitrofes:
                                    pais_objeto.limitrofes.append(posible_vecino)
                                if pais_objeto not in posible_vecino.limitrofes:
                                    posible_vecino.limitrofes.append(pais_objeto)
                                break
                    break

##########################################################################################################################################

# Lista de paises a analizar, junto con los limitrofes reales de cada uno:
paises_latinoamericanos = [
    {"nombre": "Argentina","capital": "Buenos Aires", "poblacion": 47000000, "limitrofes": ["Bolivia", "Brasil", "Chile", "Paraguay", "Uruguay"]},
    {"nombre": "Chile","capital": "Santiago", "poblacion": 19500000, "limitrofes": ["Argentina", "Bolivia", "Perú"]},
    {"nombre": "Bolivia","capital": "La Paz / Sucre", "poblacion": 12000000, "limitrofes": ["Argentina", "Brasil", "Chile", "Paraguay", "Perú"]},
    {"nombre": "Paraguay","capital": "Asunción", "poblacion": 7200000, "limitrofes": ["Argentina", "Bolivia", "Brasil"]},
    {"nombre": "Uruguay","capital": "Montevideo", "poblacion": 3500000, "limitrofes": ["Argentina", "Brasil"]},
    {"nombre": "Brasil","capital": "Brasilia", "poblacion": 215000000, "limitrofes": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Perú", "Surinam", "Uruguay", "Venezuela", "Guayana Francesa"]},
    {"nombre": "Perú","capital": "Lima", "poblacion": 34000000, "limitrofes": ["Bolivia", "Brasil", "Chile", "Colombia", "Ecuador"]},
    {"nombre": "Ecuador","capital": "Quito", "poblacion": 18000000, "limitrofes": ["Colombia", "Perú"]},
    {"nombre": "Colombia","capital": "Bogotá", "poblacion": 52000000, "limitrofes": ["Brasil", "Ecuador", "Panamá", "Perú", "Venezuela"]},
    {"nombre": "Venezuela","capital": "Caracas", "poblacion": 28000000, "limitrofes": ["Brasil", "Colombia", "Guyana"]}
    ]

# Inicio el programa tomando la lista precargada.
lista_paises_cargados = Paises.obtener_paises(paises_latinoamericanos) # Punto A carga los paises en el objeto
Paises.construccion_limitrofes(lista_paises_cargados, paises_latinoamericanos) # Punto B hace la relacion bidireccional de los limitrofes solo entre los trabajados

# Muestro al usuario paises de los que puedo seleccionar
messagebox.showinfo(
    message= f'{[paises.nombre for paises in lista_paises_cargados]}', 
    title="Paises para seleccionar")

seleccion = input("¿Qué pais quiere elegir?")

for busqueda in lista_paises_cargados:
    if busqueda.nombre.lower() == seleccion.lower():
        print(f'Su pais elegido es: {seleccion}\n Y los limitrofes de {seleccion} son: {[pais.nombre for pais in busqueda.limitrofes]}')

# %%
# Versión de mis primeros intentos mezcaladas - si llego presentaré una tercera respuesta al ejerccio 3 - Tiene fallas  (lo dejo ya que el acceso a la API es correcto y me sirve para futuro)

import random
import requests
from tkinter import messagebox

class Pais: # Creo el objeto pais con los atributos iniciales para rellenarlos con la lista
    def __init__(self, nombre: str, capital: str, poblacion: int, limitrofes) -> None:
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.limitrofes = limitrofes 

    def construccion_limitrofes(lista_paises_objeto, lista_original):
        for pais_objeto in lista_paises_objeto:
            # Buscamos el diccionario original que coincide con este país
            for pais_dic in lista_original:
                if pais_dic["nombre"] == pais_objeto.nombre:
                    # Si encontramos el país, trabajamos con su lista de limítrofes
                    for nombre_vecino in pais_dic["limitrofes"]:
                        for posible_vecino in lista_paises_objeto:
                            if posible_vecino.nombre == nombre_vecino:
                                if posible_vecino not in pais_objeto.limitrofes:
                                    pais_objeto.limitrofes.append(posible_vecino)
                                if pais_objeto not in posible_vecino.limitrofes:
                                    posible_vecino.limitrofes.append(pais_objeto)
                                break
                    break

def obtener_paises_por_region(region: str, cantidad): # luego de instalar request e importarlo accedo a la API 
    url = f"https://restcountries.com/v3.1/region/{region}" # establezco la URL y con la informacion de pais por continente
    respuesta = requests.get(url) # Guardo la repuesta del requests

    if respuesta.status_code != 200: # Cuando el requests devuelve un código diferente a 200 es por que no se puede procesar el pedido
        return None
    
    datos = respuesta.json() # Convierto el (JavaScript Object Notation) que devuelve el requests en un diccionario del que extraeré los datos 
    lista_paises = [] # Creo una lista para guardar los objetos
    seleccionados = random.sample(datos, min(cantidad, len(datos)))  # elige al azar
    
    for p in seleccionados: # Creo las instancias del objeto tomando los datos de la lista_paises
        nombre = p.get("name", {}).get("common", "Desconocido") # {} y "Desconocido" cargan valores en caso de no encontrar nada / "common" es necesario por como estan los datos en la API
        capital = p.get("capital", ["Desconocida"])[0] # accedo al nombre de la primer capital
        poblacion = p.get("population", 0) # guardo la poblacion
        limitrofes = p.get("borders",[]) # guardo los limítrofes
        pais = Pais(nombre, capital, poblacion, limitrofes) # guardo todas las variables accedidas como atributos del objeto
        lista_paises.append(pais) # armo una lista con los objetos

    return lista_paises

# Tomo los datos de la API para generar una lista de paises Random que serán con los que trabajo - solo estos deberan aparecer el los limitrofes a mostrar en el punto 3
messagebox.showinfo(
    message= f'{"Lista de Regiones disponibles en API: Africa, Americas, Asia, Europe, Oceania"}', 
    title="Regiones")

region = input("¿Que región quiere elegir para extraer paises?") # Input simepre devuelve string
cantidad_paises = input('¿Cuántos paises quiere analizar?')

paises_region = obtener_paises_por_region(region, int(cantidad_paises))

# Lista para resolver problema de abreviaturas

lista_original = []
for p in paises_region:
    pais_dict = {
        "nombre": p.nombre,
        "limitrofes": list(p.limitrofes)  # hacemos una copia de la lista de strings
    }
    lista_original.append(pais_dict)

# Contrumos los limitrofes
Pais.construccion_limitrofes(paises_region, lista_original)

# Muestro al usuario paises de los que puedo seleccionar
messagebox.showinfo(
    message= f'{[pais.nombre for pais in paises_region]}', 
    title="Paises para seleccionar")

seleccion = input("¿Qué pais quiere elegir?")

for busqueda in paises_region:
    if busqueda.nombre.lower() == seleccion.lower():
        print(f'Su pais elegido es: {seleccion}\n Y los limitrofes de {seleccion} son: {[pais.nombre for pais in busqueda.limitrofes]}')


