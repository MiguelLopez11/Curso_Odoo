import Apellidos



def Nombre():
    print("¿Como te llamas?")
    Nom = input()
    return Nom

def GetApellidos():
    Nom = Nombre()
    Apell = Apellidos.Apellidos()

    print(f"¡Bienvenido {Nom, Apell}!")


GetApellidos()
