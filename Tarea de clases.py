class Bio:
  def __init__(self, nombre, edad, sexo, nacionalidad):
    self.nombre= nombre
    self.edad = edad
    self.sexo= sexo
    self.nacionalidad= nacionalidad

  def mostrar_datos(self):
      print("Persona: ", self.nombre, ",", self.edad, ",", self.nacionalidad.lower(), ",", "sexo ", self.sexo.lower(), ".")

class Formacion(Bio):
  def __init__(self, nombre, edad, sexo, nacionalidad, grado, universidad, master):
    super().__init__(nombre, edad, sexo, nacionalidad)
    self.grado = grado
    self.universidad= universidad
    self.master = master

  def mostrar_educ(self):
      print("Educación: estudió ", self.grado.lower(), "en la ", self.universidad, " y cursó un master en ", self.master,".")

class Entret(Formacion):
  def __init__(self, nombre, edad, sexo, nacionalidad, grado, universidad, master, hobby):
    super().__init__(nombre, edad, sexo, nacionalidad, grado, universidad, master)
    self.hobby= hobby

  def mostrar_todo(self):
    print("Persona: ", self.nombre, ",",self.edad, ",", self.nacionalidad.lower(), ",", "sexo ", self.sexo.lower(), ".",
    "Educación: estudió ", self.grado, "en la ", self.universidad, " y cursó un master en ", self.master,".", "Su pasatiempo favorito es ", self.hobby.lower(), ".")

  def mostrar_hobby(self):
    print("Su pasatiempo favorito es ", self.hobby.lower(), ".")

candidato1= Entret("Carlos Corominas","29 años","Masculino", "Dominicano", "Ingeniería", "UNIBE", "Ciencias Actuariales", "Jugar tenis")
candidato2= Entret("Amy Lebrón", "28 años", "Femenino", "Dominicana", "Economía", "UASD", "Big Data", "Patinar")
candidato3= Entret(input("Introduzca su nombre: "), input("Introduzca su edad: "), input("introduzca sexo de nacimiento: "), input("Introduzca su nacionalidad: "), input("introduzca grado cursado: "), input("introduzca universidad: "), input("introduzca master que cursó o está cursando: "), input("Introduzca Hubby: "))


candidato1.mostrar_todo()
candidato2.mostrar_todo()
candidato3.mostrar_todo()
