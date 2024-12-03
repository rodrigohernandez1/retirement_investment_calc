#cargar las librerías que voy a usar durante el proyecto 
from datetime import datetime 
import afore_module_functions as afore

#tomar la fecha de hoy: año, mes y día
date_now = datetime.now()
year_now = date_now.year
month_now = date_now.month
day_now = date_now.day

#preguntar por los datos del usuario 
name = input("ingrese su nombre\n")
#sacar las variables del día, mes y año de nacimiento
birth_year = int(input(f'¿En que año naciste {name}? Favor de ingresarlo en formato aaaa\n'))
age = year_now - birth_year #lo tomé así en vez de directo ya que necesito la edad cumplida al final del año

birth_month = int(input('Ingresa el número del mes en el cual naciste del 01 al 12 en formato mm\n'))
birth_day = int(input(f'¡Fantástico {name}! Ingresa el día en que naciste en formato dd\n'))
#validar entradas 



risk_opinion = int(input("del uno al 10 cálifique su tolerancía al riesgo, 1 que quiere tomar el MENOR riesgo posible y 10 es que le encanta el riesgo\n"))
#checar fallas de entrada del 1 al 10 
if risk_opinion < 1 or risk_opinion > 10: 
    risk_opinion = int(input("ingrese una calificación válida del 1 al 10\n"))
salary = float(input("ingrese su salario mensual\n"))
#checar fallas de entrada del 1 al 10 
if salary < 0: 
    salary = float(input("ingrese un salario válido\n"))

salario_minimo = 7568 #el salario minimo por mes en México al 30 de Nov del 2024
max_aportacion = 7568 * 23 #el tope de aportación contributiva parcial al AFORE en México es 23 veces el salario mínimo

########################################################################
#carga y lectura de archivos del AFORE, y rendimientos de diferentes activos de inverrsión
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

#cargar el archivo de grupos de edades de las 10 diferentes SIENFORES del Gobierno de México, checar apéndice 2
with open('src/SIENFORE_groups.txt', 'r', encoding = 'utf-8-sig') as file: 
    age_groups = file.read()
age_groups = age_groups.split('\n')

afore_ages = []
for group in age_groups: 
    min_age = int(group[-13:-11]) #lugar en cada línea donde se encuntra la edad mínima de ese grupo 
    max_age = int(group[-8:-6]) #lo mismo con la edad máxima 
    age_ranges = (min_age, max_age) #utilizo una tupla para que no lo edite con otros procesos 
    afore_ages.append(age_ranges) #agrego cada rango de edades a una lista 


#indexar los diccionarios para que sean más fáciles de usar 
index = []
for i in range(len(afore_groups)): 
    index.append(i)
afore_returns_indexed = dict(zip(index, afore_returns))
#usare la mimsa lista de index ya que los diccionarios tienen el mismo número de claves
afore_ages_indexed = dict(zip(index, afore_ages))

########################################################################
#AFORE 
group_assignment = afore.afore_assignment(age, afore_ages_indexed) #el grupo del AFORE en el que el usuario se encuentra basado en su edad
bimestral_contribution = afore.afore_default_contribution(salary) #la contribución obligatoria y predispuesta (gobierno + empleador + empleado) por bimestre basado en el salario
years_left_group = afore.afore_years_left(age, afore_ages_indexed, month_now) #años que quedan en el grupo actua; del AFORE

print(group_assignment)
print(bimestral_contribution)
print(years_left_group)


 


    






    










    










# %%
