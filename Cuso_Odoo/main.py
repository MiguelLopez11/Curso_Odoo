import Apellidos


class Nombre:
    def __init__(self):
        print("")
    def Nombre(self):
        print("¿Como te llamas?")
        self.Nom = input()

    def GetApellidos(self):
        self.Apell = Apellidos.Apellidos()

        print(f"¡Bienvenido {self.Nom, self.Apell}!")




Nombre.Nombre()
Nombre.GetApellidos()