

class estudiante:
    def __init__(self, nombre, edad, genero) -> None:

        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def estudiar():

        print(f'estudiando...')


nombre = input('Ingrese su nombre ')
edad = input('Ingrese su edad ')
genero = input('Ingrese su genero ')


estudiante_1 = estudiante(nombre, edad, genero)

print(f'''
      
      DATOS DEL ESTUDIANTE \n
      
      nombre: {estudiante_1.nombre}\n
      edad: {estudiante_1.edad}\n
      genero: {estudiante_1.genero}\n
      
      ''')


while True:
    estudiar = input()

    if estudiar.lower() == 'estudiar':
        estudiante.estudiar()
