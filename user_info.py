#cargar las librerías que voy a usar durante el proyecto 
#import yfinance as yf 

#preguntar por los datos del usuario 
name = input("ingrese su nombre")
age = int(input("ingrese su edad como número entero"))
#checar fayas de entrada de edad
if age < 18 or age >= 65 or type(age) != int:
    age = int(input("ingrese una edad válida del 18 al 64"))
risk_opinion = int(input("del uno al 10 cálifique su tolerancía al riesgo, 1 que quiere tomar el MENOR riesgo posible y 10 es que le encanta el riesgo"))



