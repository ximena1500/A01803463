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
print(" Estado actualizado de la lista:")
for i in range(len(articulos)):
    estado = "Comprado" if comprado[i] else "Pendiente"
    print(f"  - {articulos[i]}: {estado}")
