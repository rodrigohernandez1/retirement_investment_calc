#en este modulo escribo todas las funciones que tienen que ver con el calculo de interés del AFORE, asignación de grupo del AFORE,, cantidad de años en el grupo corriente y más 

def afore_assignment(age, afore_dict):
    """
    Esta función asigna el grupo de SIENFORE en el que se encuentra el usuario dependiendo de su edad 

    Parameters
    ----------
    age :  int 
        es la edad del usuario 
    afore_dict: dict
        es un diccionario con el rango de edades como valor de el grupo de AFORE como clave. 

    Returns
    -------
    el grupo de SIENFORE en el que se encuentra el usuario 

    """ 
    for group in afore_dict:
        age_range = afore_dict[group]
        if age <= age_range[1] and age >= age_range[0]: #busca si la edad está entre el rango de edad de la tupla
            return group
def afore_default_contribution(salary): 
    """
    Esta función calcula la contribución total al AFORE bimestralmente basada en el salario sin contar las contribuciones voluntarias 

    Parameters
    ----------
    salary :  float 
        el salario del usuario 

    Returns
    -------
    contribución total al AFORE sin contribuciones voluntarias, considerando el trabajdor está dado de alta en el IMSS 

    """ 
    bimestral_salary = salary * 2 #el salario bimestral 
    worker_contribution = bimestral_salary * 0.01125 #la contribución obligatoria del trabajdor es de 1.125% del salario, y es bimestral 
    employer_contribution = bimestral_salary * 0.0515 #contribución del empleador es de 5.15% del salario, vease apéndice 4 
    government_contribution = bimestral_salary * 0.00225 #la contribución del goberino sobre tu salario
    total_contribution = worker_contribution + employer_contribution + government_contribution
    return total_contribution

        
