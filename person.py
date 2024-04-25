class personas:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni 
    def GetNombre(self): return self.nombre
    def GetEdad(self): return self.edad
    def GetDni(self): return self.dni
    def ShowData(self):
        print(self.nombre)
        print(self.edad)
        print(self.dni)
    def High(self):
        if int(self.edad) >= 18: return True
        return False
    @staticmethod
    def GenPersons(List):
        newlist = []
        for person in List: newlist.append(personas(person[0], person[1], person[2]))
        return newlist
    def ShowPersons(List):
        for persona in List:
            if persona.High():
                print(persona.GetNombre() + " " + str(persona.GetEdad()))

Personas = personas.GenPersons([
    ["pedro", 19, "301923019"],
    ["juan", 21, "pepe"],
    ["maria", 15, "219821"],
])
personas.ShowPersons(Personas)