import random


class JuegoAdivinanza:

    def __init__(self):
        print('-----Juego de Adivinanzas-----')
        self.numero_random = random.randint(0, 5)
        self.intentos = 0

    def ejecutar(self):
        while True:

            opcion = (int(input('Introduce el numero que crees que es correcto (1 al 5): ')))
            self.intentos += 1

            if self.numero_random == opcion:
                print(f'El numero aleatorio es {self.numero_random} y tu has dicho el {opcion}')
                print(f'Numero de intentos: {self.intentos} veces')
                print('Has ganado maquina')
                break  # si acierta termina el juego
            else:

                print('Incorrecto, intentalo de nuevo')

        print('Gracias por jugar')


prueba = JuegoAdivinanza()
prueba.ejecutar()
