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

    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)

    def es_valida(self, clave):
        if self.contiene_caracter_especial:
            return True
        return False
    
    def contiene_caracter_especial(self, clave: str) -> bool:
        for caracter in clave:
            if caracter in '@_#$%':
                return True
        return False
    
class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)


    def es_valida(self, clave):
        return super().es_valida(clave)
    
    def contiene_calisto(self, clave: str) -> bool:
        if 'calisto' in clave.lower():
            caracter_mayus = 0
            for caracter in clave:
                if caracter.isupper():
                    caracter_mayus += 1
            if caracter_mayus >= 2 and caracter_mayus < len(clave):
                return True
            return False
        return False
