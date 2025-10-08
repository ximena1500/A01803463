#temperatura 
temperaturas =  (29, 18, 22,25,15)            
promedio = sum(temperaturas) / len(temperaturas )
print(f"temperatura promedo: {promedio:}°C")

print("Dias por encima del promedio:")
for i, temp in enumerate(temperaturas):
    if temp > promedio:
       print(f" Día {i+1}: {temp}°C")

print("Dias normales o debajo del promedio:")
for i, temp in enumerate(temeraturas) : 
   if temp <= promedio:
      print(f" Dia {i+1}: {temp}°C")



#calificaciones 

estudiantes = ["Jorge", "Ximena", "Carlos", "Yazmín", "Sofia"]
calificacion = [85, 77, 90, 50, 98]

for i in range(num_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))

aprobados = 0
for calificacion in califiacacion:
    if calificacion >= 70:
       aprobados += 1

porcentaje_aprobados = (aprobados / len(calificacion)) * 100
print (f"porcentaje de aprobados: {porcentaje_aprobados:.2f}%")


#Compras 
articulos = ["Pan", "Leche", "Huevos", "Café", "Manzanas"]
comprado = [False, False, True, False, False]

print("Artículos que aún no has comprado:")
for i in range(len(articulos)):
    if not comprado[i]: 
        print(f"  - {articulos[i]}")

for i in range(len(articulos)):
    if not comprado[i]:
        respuesta = input(f"¿Ya compraste '{articulos[i]}'? (s/n): ").lower()
        if respuesta == "s":
            comprado[i] = True
print("/n Estado actualizado de la lista:")
for i in range(len(articulos)):
    estado = "Comprado" if comprado[i] else "Pendiente"
    print(f"  - {articulos[i]}: {estado}")

#mayor menor

num = int(input("¿Cuántos números ingresaras?"))
numeros = [2, 6, 8, 12, 7, 10]

for i in range(num) :
    nume = float(input(f"ingrese numero {i + 1}: "))
    numeros.append(nume)

mayor = may(numeros)
menor = men(numeros)
promedio = sum(numeros) / len(numeros)


print("/num Resultados:") 
print(f" numero mayor: {mayor}")
print(f" numero menor: {menor}")
print(f" proemdio: {promedio: .2f}")


#inventario de productos 

alimentos = ["pollo", "aguacate", "leche", "yogurt", "tortillas"]
cantidad = [5, 15, 10, 2, 20]
print("inventario actual:")
for i in range(len(productos)):
    print(f" - {alimentos[i]}: {cantidades [i]} unidades")

producto_actualizar = input("/n nombre del producto que debe de actualizarse: ")

if producto_actualizar in alimentos :
    index = productos.index(producto_actualizar)
    nueva_cantidad = int(input(f"nueva cantidad para {producto_actualizar}: "))

else:
    print("producto inexistente.")

print("\n Inventario actualizado:")
for i in range(len(productos)):
    print(f"  - {productos[i]}: {cantidades[i]} unidades")

print("\n Productos AGOTADOS:")
agotados = False
for i in range(len(productos)):
    if cantidades[i] == 0:
        print(f"  - {productos[i]}")
        agotados = True

if not agotados:
    print("  (No hay productos agotados)")

t = int(input("¿Cuántas tareas deseas agregar a tu lista? "))
tareas = ["matematicas", "ingles", "quimica"]
estado = ["true","false", "false"]

for i in range(n):
    tarea = input(f"Ingrese la tarea #{i + 1}: ")
    tareas.append(tarea)
    estado.append(False) 
print("\n Tareas pendientes:")
for i in range(len(tareas)):
    if not estado[i]:
        print(f"{i + 1}. {tareas[i]}")

marcar = input("\n¿Deseas marcar alguna tarea como completada? (s/n): ")

if marcar == "s":
    while True:
        num = int(input("Ingresa el número de la tarea completada (0 para salir): "))
        if num == 0:
            break
        if 1 <= num <= len(tareas):
            estado[num - 1] = True
        else:
            print("Número inválido.")

print("\n Tareas COMPLETADAS:")
completadas = False
for i in range(len(tareas)):
    if estado[i]:
        print(f"{tareas[i]}")
        completadas = True
if not completadas:
    print("(Aún no has completado ninguna tarea)")

print("\n Tareas PENDIENTES:")
pendientes = False
for i in range(len(tareas)):
    if not estado[i]:
        print(f"- {tareas[i]}")
        pendientes = True
if not pendientes:
    print("(No tienes tareas pendientes)")
