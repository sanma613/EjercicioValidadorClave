from validadorclave.modelo.validador import ReglaValidacion, Validador, ReglaValidacionCalisto, ReglaValidacionGanimedes
from validadorclave.modelo.errores import ValidadorError

def validar_clave(clave: str, reglasValidacion: list[ReglaValidacion]):
    try:
        for regla in reglasValidacion:
            re = Validador(regla())
            status = re.es_valida(clave)
    except ValidadorError as e:
        print(f'Error: {regla.__name__}: {e}')
    else:
        print(f'La clave es valida para {regla.__name__}')