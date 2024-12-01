#cargar las librerías que voy a usar durante el proyecto 
#import yfinance as yf 

#preguntar por los datos del usuario 
name = input("ingrese su nombre\n")
age = int(input("ingrese su edad como número entero\n"))
#checar fallas de entrada de edad, 
if age < 16 or age >= 99: #la edad es de mínima de 16 ya que es la edad mínima para esta en IMSS en México y tomaré 99 como el límite de edad aquí 
    age = int(input("ingrese una edad válida del 18 al 64\n"))
risk_opinion = int(input("del uno al 10 cálifique su tolerancía al riesgo, 1 que quiere tomar el MENOR riesgo posible y 10 es que le encanta el riesgo\n"))
#checar fallas de entrada del 1 al 10 


#cargar el archivo de grupos de edad de las 10 diferentes SIENFORES, checar apéndice 1
with open('src/SIENFORE_groups.txt', 'r', encoding = 'utf-8-sig') as file: #el encoding le quita el "ufeff" de formato que le pone el editor de texto
    afore_groups = file.read()
afore_groups = afore_groups.split('\n')
print(afore_groups)

age_groups = [] #grupos de edad que AFORE categoriza
for group in afore_groups:
    max_age = group[-8:-6] #estos son los lugares de edad máxima en cada lista de las categorias de AFORE
    min_age = group[-13:-11] #estos son los lugares de edad mínima en cada lista de las categorias de AFORE 
    age_ranges = (min_age, max_age)
    age_groups.append(age_ranges)
print(age_groups)

    









