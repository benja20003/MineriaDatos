# Title: Ejemplo de programación orientada a objetos
# Description: Ejemplo de programación orientada a objetos en Python

# Autor: Eduardo Jeraldo

import numpy as np

class Rectangulo:
    '''
    Clase que representa un rectángulo
    '''
    def __init__(self, base : float, altura: int) -> None:
        self.base = base
        self.altura = altura

    def area(self):
        '''	
        Calcula el area del rectángulo
        '''
        return self.base * self.altura

    def perimetro(self):
        '''
        Calcula el perímetro del rectángulo
        '''
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        '''	
        Representación en string del rectangulo
        '''
        return f"Rectangulo de base {self.base} y altura {self.altura}"
    
class Cuadrado(Rectangulo):
    
    def __init__(self, lado: float) -> None:
        super().__init__(lado, lado)
        
    def __str__(self):
        return f"Cuadrado de lado {self.base}"
    
    @property
    def lado(self):
        return self.base
    
    @lado.setter
    def lado(self, valor):
        self.base = valor
        self.altura = valor
        
        
def main():
    r = Rectangulo(2, 3)
    print(r)
    print(f"Area: {r.area()}")
    print(f"Perimetro: {r.perimetro()}")

    c = Cuadrado(4)
    print(c)
    print(f"Area: {c.area()}")
    print(f"Perimetro: {c.perimetro()}")

    c.lado = 5
    print(c)
    print(f"Area: {c.area()}")
    print(f"Perimetro: {c.perimetro()}")

    print(np.random.random(5))
    
if __name__ == "__main__":
    main()