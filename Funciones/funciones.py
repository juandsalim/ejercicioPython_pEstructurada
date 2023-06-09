import os
import ast



def main():
    menu()

#funcion para el menu
def menu():
    listaEmpleados= []
    op=False
    while not op:
        os.system("cls")
        print("***************************************************")
        print(" === M E N Ú === ")
        print(" 1- Ingresar un empleado nuevo")
        print(" 2- Consultar lista de empleados ")
        print(" 3- Buscar empleado")
        print(" 4- Mostrar promedio de los sueldos")
        print("5- Salir")
        print("***************************************************")
        op=int(input("Ingresar la opción "))
        if op==1:
            listaEmpleados = ingresarEmpleados(listaEmpleados)
            op = False
        elif op==2:
            mostrarEmpleados(listaEmpleados)
            input()
            op = False
        elif op==3:
            os.system("cls")
            buscarEmpleado(listaEmpleados)
            input()
            op=False
        elif op ==4:
            calcularPromedio(listaEmpleados)
            input()
            op = False
        elif op ==5:
            op=True
        else:
            print("No es una opción válida")
            input()
            menu(listaEmpleados)



# funcion para agregar nuevos empleados
def ingresarEmpleados(listaEmpleados):
    
    l=[input("Ingrese el nombre "),input("Ingrese el apellido "),float(input("Ingrese el salario "))]
    
    listaEmpleados.append(l)
    f=open("empleados.txt","w")
    for empleado in listaEmpleados:
        f.write(str(empleado) + '\n')
    f.close()
    return listaEmpleados

# funcion para calcular el promedio
def calcularPromedio(listaEmpleados):

    totalSueldos = sum(l[2] for l in listaEmpleados)
    promedio = totalSueldos / len(listaEmpleados)
    print(f"El sueldo promedio es {promedio}")
        
# mostrar empleados
def mostrarEmpleados(listaEmpleados):
    os.system("cls")
    f=open("empleados.txt","r")
    lineas = f.readlines()
    for linea in lineas:
        elemento = ast.literal_eval(linea)
        
        print("Nombre: {}, Apellido: {}, Salario: {}".format(*elemento))
        listaEmpleados.append(elemento)
       
    
# funcion ´para busca el empleado por nombre
def buscarEmpleado(listaEmpleados):
    
    elemento = input('ingrese el nombre ')
    #empleo una doble iteracion ya que la lista contiene otras listas
    for i, nombre in enumerate(listaEmpleados): # enumerate me devuelve una tupla de dos elementos.
        
        try:
            indice = nombre.index(elemento)
            
            print(listaEmpleados[i])
            return i, indice
           
        except ValueError:
            pass
    print("No se encontro el empleado")
    return None, None

