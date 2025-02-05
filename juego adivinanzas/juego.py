import random


class JuegoAdivinanza:

    def __init__(self):
        print('-----Juego de Adivinanzas-----')
        self.numero_random = random.randint(0, 5)
        self.intentos = 0

    def ejecutar(self):

        self.menu_juego()

        while self.intentos < self.max_intentos:
            try:
                opcion = (int(input('Introduce el numero que crees que es correcto (1 al 5): ')))
                self.intentos += 1

                if self.numero_random == opcion:
                    print(f'¡Correcto! El número era {self.numero_random}.')
                    print(f'Intentos: {self.intentos}/{self.max_intentos}')
                    print('Has ganado maquina!')
                    break  # si acierta termina el juego
                else:
                    print('Pista: Es más grande...' if self.numero_random > opcion else 'Pista: Es más pequeño...')
                    print(f'Intentos restantes: {self.max_intentos - self.intentos}')

            except ValueError as e:
                print('Introduce un numero, las letras no son validas!')

        else:
            print(f'¡Game Over! El número era {self.numero_random}. ¡Sigue practicando!')

        print('¡Gracias por jugar!')

    def menu_juego(self):
        while True:
            print('Elige un nivel:')
            print('Nivel 1 (Máx 8 intentos):')
            print('Nivel 2 (Máx 5 intentos):')
            print('Nivel 3 (Máx 2 intentos):')

            try:
                opcion_nivel = int(input('Elige un nivel (1-3): '))

                if opcion_nivel == 1:
                    self.max_intentos = 8
                elif opcion_nivel == 2:
                    self.max_intentos = 5
                elif opcion_nivel == 3:
                    self.max_intentos = 2
                else:
                    print("Opción no válida. Elige 1, 2 o 3.")
                    continue

                break  # Sale del bucle si la elección es válida

            except ValueError:
                print("⚠️ Entrada no válida. Introduce un número del 1 al 3.")


