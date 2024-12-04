#cargar las librerías que voy a usar durante el proyecto 
from datetime import datetime 
import afore_module_functions as afore
import interest_module as interest

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
#validar entradas 
while age >= 65: 
    birth_year = int(input('Esta calculadora no acepta edades mayores que 64 años, lo sentimos. Por favor ingrese una edad válida'))
    age = year_now - birth_year
while age < 16: 
    birth_year = int(input('Tienes que tener 16 años mínimo para empezar a trabajar en México formalmente, favor de ingresar un año válido'))
    age = year_now - birth_year 
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
afore_total = 0 

group_assignment = afore.afore_assignment(age, afore_ages_indexed) #el grupo del AFORE en el que el usuario se encuentra basado en su edad
bimestral_contribution = afore.afore_default_contribution(salary) #la contribución obligatoria y predispuesta (gobierno + empleador + empleado) por bimestre basado en el salario
months_left_current_group = afore.afore_months_left(age, afore_ages_indexed, month_now) #años que quedan en el grupo actua; del AFORE

current_annual_return = afore_returns_indexed[group_assignment]
bimesters_left_group = months_left_current_group // 2  #medio mes en cada bimestre, las aportaciones al AFORE son bimestrales. Y solo cuento bimestres completos
current_bimestral_return = interest.interest_period_change(current_annual_return, 2)

#asumiré que las aportaciones se hacen al inicio después de cada bimestre de trabajo. Ejemplo si se trabajo ENERO y FEBREO entonces la aportación se hace el 5 de Marzo.
for t in range(0, bimesters_left_group): #dada la asunción previa, el rango es del 0 para el bimestre que no tuvo rendimientos (el último) y es -1 la cantidad de bimestres ya que empiezas 2 meses después de empezar el trabajo 
    afore_total += bimestral_contribution * ((1 + current_bimestral_return/100) ** t) #formúla de interés compuesto cada bimestre


while group_assignment <= 7:  
    group_assignment += 1 # moverte al sigiente grupo
    
    beggining_principal = afore_total #principal al principio de el periodo 
    new_annual_return = afore_returns_indexed[group_assignment] #retorno anual del siguiente grupo del AFORE
    new_bimestral_return = interest.interest_period_change(new_annual_return, 2) #nuevo interés bimestral 

    gained_on_principal = beggining_principal * ((1 + new_annual_return/100) ** 5) #cinco años compuesto 
    bimesters_left_group = 5 * 6 #5 años por grupo después del primero (Básica Inicial) y 6 bimestres por año 
    bimestral_gain = 0 
    for t in range(0, bimesters_left_group): #dada la asunción previa, el rango es del 0 para el bimestre que no tuvo rendimientos (el último) y es -1 la cantidad de bimestres ya que empiezas 2 meses después de empezar el trabajo 
        bimestral_gain += bimestral_contribution * ((1 + new_bimestral_return/100) ** t) #formúla de interés compuesto cada bimestre
    
    afore_total = gained_on_principal + bimestral_gain 

afore_total = round(afore_total, 2)
print(f'Asumiendo su ingreso aumente con relación a la inflación y contando las aportaciones desde hoy, al cumplir los 65 años te retirarás con {afore_total}')





 


    






    










    









