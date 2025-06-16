stock = 20
reserva= []

def reservas():
        global stock
        nombre=input("Ingrese su nombre: ")
        frase=input("Ingresar frase secreta: ")
        if frase == "EstoyEnListaDeReserva":
            persona = {"nombre": nombre ,"estado": 'normal'}
            for F in reserva:
                if persona['nombre'] == F['nombre']:
                    print('esta persona ya reservo')
                    return
            reserva.append(persona)
            print("La reserva se ejecuto correctamente")
            stock-=1

           
        else:
            print("error...!!!!")

def buscar():
    global stock
    nombre=input("Nombre de reserva: ")
    for F in reserva:
        if F["nombre"] == nombre:
            print('se encontro su reserva')
            print("¿Desea pagar adicional para VIP y reservar 2 pares?")
            vip=input("S/N: ").lower()
            if vip == "s":
                F["estado"] = 'vip'
                stock-=1
            else:
                print("Saliendo de busqueda.")

def cancelar():
    nombre=input('Ingrese el nombre de quien quiere eliminar de la reserva: ')
    for F in reserva:
        if F['nombre'] == nombre:
            reserva.remove(F)
            print(f"La reserva de {nombre} sido cancelada.")

        
def menu():

    print("***TOTEM AUTOATENCIÓN RESERVA STRIKE***\n1. Reservar\n2. Buscar zapatillas\n3. Cancelar Reserva de zapatillas\n4. Salir")
    while True:
        try:
            op=int(input("eligir opcion: "))
        
            if op == 1:
                if stock<=0:
                    print('ya no queda stock')
                else:
                    reservas()    
            elif op == 2:
                buscar() 
            elif op == 3:
                cancelar()
            elif op == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opcion valida!!")
        except ValueError:
            print('ingreso una opcion no valida')

menu()