#este modulo contiene todas las funciones para calcular interes compuesto, cambio de periodos, retornos ...
def interest_period_change(annual_return, months):
    """
    Esta función cambia el interés anual a interés equivalente compuesto en un periodo diferente al anual.  

    Parameters
    ----------
    annual_return :  float 
        el retorno anual que quiere ser convertido a otro periodo, expresado como porcentaje (5.7% se escribe sin el signo: 5.7) 
    months: int
        los meses al cual el interés será convertido. 

    Returns
    -------
    period_rate convertido compuesto 

    """ 
    if months == 0: 
        raise ValueError("months tiene que ser mayor que 0") 
    base = 100
    final = 100 * (1 + (annual_return/100))
    period_fraction = 12 / months #la fracción del periodo con relación a un año, si el periodo son 2 meses, la fracción es 1/6 ya que hay 6 bimestres en el año
    period_rate = (final/base)**(1/period_fraction) - 1
    period_rate_percentage = period_rate * 100
    return period_rate_percentage
