from abc import ABC, abstractmethod

class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada = longitud_esperada
    
    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

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

    def es_valida(self, clave):
        if self.contiene_caracter_especial:
            return True
        return False
    
    def contiene_caracter_especial(self, clave: str) -> bool:
        for caracter in clave:
            if caracter in '@_#$%':
                return True
        return False

