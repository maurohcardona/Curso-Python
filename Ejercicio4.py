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
        print(f'Los instumentos de tipo {TipoInstrumento} son: ')
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.tipoInstrumento == TipoInstrumento:
                    print(instrumento.nombre)

    def borrar_instrumento(self, id):
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.id == id:
                    sucursal.instrumentos.remove(instrumento)

    def porcentaje_instrumento_tipo(self):
        viento = 0
        cuerdas = 0
        percusion = 0
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.tipoInstrumento == TipoInstrumento.CUERDAS.value:
                    cuerdas += 1
                elif instrumento.tipoInstrumento == TipoInstrumento.VIENTO.value:
                    viento += 1
                elif instrumento.tipoInstrumento == TipoInstrumento.PERCUSION.value:
                    percusion += 1
        porcentaje_viento = (viento / len(sucursal.instrumentos)*100)
        porcentaje_cuerdas = (cuerdas / len(sucursal.instrumentos)*100)
        porcentaje_percusion = (percusion / len(sucursal.instrumentos)*100)
        print(f'''
            portcentaje cuerdas: {porcentaje_cuerdas}%
            porcentaje viento: {porcentaje_viento}%
            porcentaje percusion: {porcentaje_percusion}%''')


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
instrumento2 = Instrumento("2", "Flauta", 100, TipoInstrumento.VIENTO.value)
instrumento3 = Instrumento("3", "Violin", 100, TipoInstrumento.CUERDAS.value)
instrumento4 = Instrumento("4", "Tambor", 100, TipoInstrumento.PERCUSION.value)

sucursal1.agregar_instrumento(instrumento1)
sucursal1.agregar_instrumento(instrumento2)
sucursal1.agregar_instrumento(instrumento3)
sucursal1.agregar_instrumento(instrumento4)

fabrica.ver_sucursales()

fabrica.listar_instrumentos()

fabrica.listar_instrumentos_tipo(TipoInstrumento.VIENTO.value)

# fabrica.borrar_instrumento("2")

# fabrica.listar_instrumentos()

fabrica.porcentaje_instrumento_tipo()
