#cargar las librerías que voy a usar durante el proyecto 
#import yfinance as yf 
#import datetime as datetime

#preguntar por los datos del usuario 
name = input("ingrese su nombre\n")
age = int(input("ingrese su edad como número entero\n"))
#checar fallas de entrada de edad, 
if age < 16 or age >= 99: #la edad es de mínima de 16 ya que es la edad mínima para esta en IMSS en México y tomaré 99 como el límite de edad aquí 
    age = int(input("ingrese una edad válida del 18 al 64\n"))
risk_opinion = int(input("del uno al 10 cálifique su tolerancía al riesgo, 1 que quiere tomar el MENOR riesgo posible y 10 es que le encanta el riesgo\n"))
#checar fallas de entrada del 1 al 10 


#cargar el archivo de grupos de rendimientos promedio en los últimos 5 años de las 10 diferentes SIENFORES del Gobierno de México, checar apéndice 1
with open('src/SIENFORE_returns.txt', 'r', encoding = 'utf-8-sig') as file: #el encoding le quita el "ufeff" de formato que le pone el editor de texto
    afore_file = file.read()
afore_file = afore_file.split('\n')


afore_groups = [] #grupos de edad que AFORE categoriza
afore_returns = [] #retornos por grupo de afore
for group in afore_file:
    returns = float(group[-4:])
    afore_returns.append(returns) #separando los retornos del file de texto original 
    afore_groups.append(group[0: -6]) #separando el nombre de los distintos grupos del afore, los SIENFOREs
afore_dict = dict(zip(afore_groups, afore_returns))
print(afore_dict['Básica Inicial'])








    









