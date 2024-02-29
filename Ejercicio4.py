from enum import Enum


class TipoInstrumento(Enum):
    VIENTO = "Viento"
    CUERDAS = "Cuerdas"
    PERCUSION = "Percusion"


class Fabrica():
    def __init__(self):
        self.sucursales = []

    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)

    def ver_sucursales(self):
        for sucursal in self.sucursales:
            print(sucursal.nombre)

    def listar_instrumentos(self):
        for sucursal in self.sucursales:
            print(f'Instrumentos en {sucursal.nombre}: ')
            for instrumento in sucursal.instrumentos:
                print(f'''Instrumento: {instrumento.nombre}, precio: ${
                      instrumento.precio}, tipo: {instrumento.tipoInstrumento}''')

    def listar_instrumentos_tipo(self, TipoInstrumento):
        pass

    def borrar_instrumento(self, id):
        pass

    def porcentaje_instrumento_tipo(Sucursal):
        pass


class Sucursal(Fabrica):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.instrumentos = []

    def agregar_instrumento(self, instrumento):
        self.instrumentos.append(instrumento)


class Instrumento(Sucursal):
    def __init__(self, id, nombre, precio, tipoInstrumento):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.tipoInstrumento = tipoInstrumento


fabrica = Fabrica()

sucursal1 = Sucursal("Almagro")

fabrica.agregar_sucursal(sucursal1)

instrumento1 = Instrumento("1", "Guitarra", 100, TipoInstrumento.CUERDAS.value)

sucursal1.agregar_instrumento(instrumento1)

fabrica.ver_sucursales()

fabrica.listar_instrumentos()
