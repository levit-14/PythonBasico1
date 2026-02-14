#Loops
mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print ("El numero es:", i)

resultado = 0
for i in mi_lista:
    resultado += i
print(f"El resultado de la suma de mi lista es: {resultado}")

for i in range(2, 9):
    print(i)

#while loop
i=0

while i<3:
    i += 1
    if i==3:
        continue
    print(i)
    if i == 4:
        break
    else:
        print("i es ahora mayor o igual a >")

# Practica 2
# Dada la lista mi_lista_2 = ("Lunes", "martes", "miercoles", "jueves", "viernes")
# Imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
# Pista: Usa los dos tipos loops while y for en el mismo programa para lograrlo

i = 0
mi_lista_2 = ["Lunes", "martes", "miercoles", "jueves", "viernes"]
while i < 3:
    i +=1

for d in mi_lista_2:
    if d != "lunes":
        print(d)