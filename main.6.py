print(" ")
print("Arzaba Diaz April 3W 1173")
def es_email_valido(email):
    """
    Esta funcion verifica si una direccion de email es valida.
    Una direccion es considerada valida si contiene el caracter '@'. #en esta linea
    
    Args:
    email (str): La direccion de email a verificar.

    Returns:
    bool: True si la direccion es valida, False en caso contrario.
    """
    return '@' in email

def capturar_email():
    """
    Esta funcion captura una direccion de email del usuario y despliega un mensaje
    indicando si la direccion es valida o no. #en esta linea
    """
    email = input("Introduce tu direccion de email: ")
    if es_email_valido(email):
        print("La direccion de email es valida.")
    else:
        print("La direccion de email no es valida.")

# Ejemplo de uso
capturar_email()
