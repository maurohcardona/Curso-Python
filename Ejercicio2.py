class Animal():
    def __init__(self, cantidad_patas, vertebrado):
        self.cantidad_patas = cantidad_patas
        self.vertebrado = vertebrado

    def comer():
        print('Estoy comiendo')


class Perro(Animal):
    def __init__(self, cantidad_patas, vertebrado, nombre, raza):
        super().__init__(cantidad_patas, vertebrado)
        self.nombre = nombre
        self.raza = raza

    def informacion(self):
        print(f'El perro se llama {self.nombre}, tiene {
              self.cantidad_patas} patas, es {self.vertebrado} y es de raza {self.raza}')

    def correr(self):
        print('Estoy corriendo')


class Aguila(Animal):
    def __init__(self, cantidad_patas, vertebrado):
        super().__init__(cantidad_patas, vertebrado)

    def informacion(self):
        print(f' el aguila tiene {
              self.cantidad_patas} patas, y es un {self.vertebrado}')

    def volar(self):
        print('Estoy volando')


perro1 = Perro(4, 'Vertebrado', 'bob', 'golden')
aguila1 = Aguila(2, 'vertebrado')

perro1.informacion()
perro1.correr()

aguila1.informacion()
aguila1.volar()
