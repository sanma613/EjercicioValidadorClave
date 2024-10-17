from abc import ABC, abstractmethod
from validadorclave.modelo.errores import NoTieneCaracterEspecialError, NoTieneLetraMayusculaError, NoCumpleLongitudMinimaError, NoTieneLetraMinusculaError, NoTieneNumeroError, NoTienePalabraSecretaError

class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada = longitud_esperada
    
    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        ...

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) >= self.longitud_esperada:
            return True
        return False

    def _contiene_mayuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False

class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self, longitud_esperada=9):
        super().__init__(longitud_esperada)

    def es_valida(self, clave: str):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError('La clave debe tener una longitud de más de 8 caracteres')
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError('Sin mayuscula')
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError('Sin minuscula')
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError('Sin numero')
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError('Clave sin caracteres especiales.')
        return True
    
    def contiene_caracter_especial(self, clave: str) -> bool:
        for caracter in clave:
            if caracter in '@_#$%':
                return True
        return False
    
class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self, longitud_esperada=7):
        super().__init__(longitud_esperada)

    def es_valida(self, clave: str):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError('La clave debe tener una longitud de más de 8 caracteres')
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError('Sin mayuscula')
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError('Sin minuscula')
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError('Sin numero')
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError('La palabra calisto debe estar escrita con al menos dos letras en mayúscula')
        return True
    
    def contiene_calisto(self, clave: str) -> bool:
        if 'calisto' in clave.lower():
            caracter_mayus = 0
            for caracter in clave:
                if caracter.isupper():
                    caracter_mayus += 1
            if caracter_mayus >= 2 and caracter_mayus < len('calisto'):
                return True
            return False
        return False

class Validador:
    
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str):
        status = self.regla.es_valida(clave)
        return status