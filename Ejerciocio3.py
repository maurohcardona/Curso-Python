class Empleado():
    def __init__(self, dni, nombre, apellido, ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.ingreso = ingreso


class SalarioFijo(Empleado):

    def __init__(self, dni, nombre, apellido, ingreso, sueldoBasico):
        super().__init__(dni, nombre, apellido, ingreso)
        self.sueldoBasico = sueldoBasico
        self.antiguedad = 2022 - self.ingreso

    def mostrarSalario(self):

        CAT1 = 1
        CAT2 = 1.05
        CAT3 = 1.10

        if self.antiguedad < 2:
            categoria = CAT1
        elif self.antiguedad < 10 and self.antiguedad >= 2:
            categoria = CAT2
        elif self.antiguedad >= 10:
            categoria = CAT3

        salario = self.sueldoBasico * categoria

        print(f'''El empleado {self.nombre} {self.apellido}, dni: {
              self.dni}, antiguedad de {self.antiguedad} anos cobra: ${salario}''')


class SalarioComision(Empleado):
    def __init__(self, dni, nombre, apellido, ingreso, salarioMin, clientesCap, montoPorCliente):
        super().__init__(dni, nombre, apellido, ingreso)
        self.salarioMin = salarioMin
        self.clientesCap = clientesCap
        self.montoPorCliente = montoPorCliente

    def mostrarSalario(self):
        salario = self.clientesCap * self.montoPorCliente
        if salario < self.salarioMin:
            salario = self.salarioMin
        print(f'''El empleado {self.nombre} {
              self.apellido}, dni: {self.dni} cobra: ${salario}''')


empleado1 = SalarioFijo(
    23456789, "Pedro", "Lopez", 2015, 1500.0)
empleado2 = SalarioComision(
    98765432, "Ana", "Rodriguez", 2019, 1200.0, 80.0, 100)


empleado1.mostrarSalario()
empleado2.mostrarSalario()
