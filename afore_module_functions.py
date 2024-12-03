#en este modulo escribo todas las funciones que tienen que ver con el calculo de interés del AFORE, asignación de grupo del AFORE,, cantidad de años en el grupo corriente y más 

def afore_assignment(age, afore_dict):
    """
    Esta función asigna el grupo de SIENFORE en el que se encuentra el usuario dependiendo de su edad 

    Parameters
    ----------
    age :  int 
        es la edad del usuario 

    Returns
    -------
    el grupo de SIENFORE en el que se encuentra el usuario 

    """ 
    for group in afore_dict:
        age_range = afore_dict[group]
        if age <= age_range[1] and age >= age_range[0]: #busca si la edad está entre el rango de edad de la tupla
            return group
        
