#cargar las librerías que voy a usar durante el proyecto 
#import yfinance as yf 

#preguntar por los datos del usuario 
name = input("ingrese su nombre")
age = int(input("ingrese su edad como número entero"))
#checar fallas de entrada de edad, 
if age < 16 or age >= 65: #la edad es de mínima de 16 ya que es la edad mínima para esta en IMSS en México y 64 es la edad máxima para ahorrar antes de los 65
    age = int(input("ingrese una edad válida del 18 al 64"))
risk_opinion = int(input("del uno al 10 cálifique su tolerancía al riesgo, 1 que quiere tomar el MENOR riesgo posible y 10 es que le encanta el riesgo"))





