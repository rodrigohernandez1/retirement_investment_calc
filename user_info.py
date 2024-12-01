#cargar las librerías que voy a usar durante el proyecto 
#import yfinance as yf 

#preguntar por los datos del usuario 
name = input("ingrese su nombre")
age = int(input("ingrese su edad como número entero"))
#checar fallas de entrada de edad, 
if age < 16 or age >= 120: #la edad es de mínima de 16 ya que es la edad mínima para esta en IMSS en México y 120 es más que el récord de edad más vieja de México
    age = int(input("ingrese una edad válida del 18 al 64"))
risk_opinion = int(input("del uno al 10 cálifique su tolerancía al riesgo, 1 que quiere tomar el MENOR riesgo posible y 10 es que le encanta el riesgo"))
#checar fallas de entrada del 1 al 10 


#cargar el archivo de grupos de edad de las 10 diferentes SIENFORES, checar apéndice 1
with open('src/SIENFORE_groups.txt', 'r') as file:
    afore_groups = file.read() 
    print(afore_groups)






