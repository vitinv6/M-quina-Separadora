#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import (Port, Button, Color, ImageFile,SoundFile)
from pybricks.tools import wait

# Os Quadrados Coloridos são vermelho, verde, azul ou amarelo.
POSSIBLE_COLORS = (Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW)

# Configura o motor da esteira com as configurações padrão. Este motor
# aciona a esteira transportadora.
belt_motor = Motor(Port.D)

# Configura o motor de alimentação com as configurações padrão. Este
# motor ejeta os Quadrados Coloridos.
feed_motor = Motor(Port.A)

# Configura o Sensor de Toque. Ele é usado para detectar quando o motor
# da esteira moveu o módulo de classificação totalmente para a esquerda.
touch_sensor = TouchSensor(Port.S1)

# Configura o Sensor de Cor. Ele é usado para detectar a cor dos
# Quadrados Coloridos.
color_sensor = ColorSensor(Port.S3)

# Esta é a parte principal do programa. É um loop que se repete
# infinitamente.
#
# Primeiro, ele move os 2 motores para suas posições iniciais corretas.
# Segundo, ele espera que você escaneie e insira até 8 Quadrados
# Coloridos.
# Finalmente, ele os classifica por cor e os ejeta em suas posições
# corretas.
#
# Então o processo recomeça, para que você possa escanear e inserir
# o próximo conjunto de Quadrados Coloridos.
while True:
    # Inicializa o motor de alimentação. Isso é feito executando o
    # motor para frente até que ele pare. Isso significa que ele não
    # pode se mover mais. A partir deste ponto final, o motor gira
    # para trás em 180 graus. Esta é a posição inicial.
    feed_motor.run_until_stalled(120)
    feed_motor.run_angle(450, -180)

    # Inicializa o motor da esteira transportadora. Isso é feito
    # primeiro executando o motor da esteira para trás até que o
    # Sensor de Toque seja pressionado. Então o motor para e o ângulo
    # é resetado para "0." Isso significa que, quando ele girar para
    # trás para "0" mais tarde, ele retornará a esta posição inicial.
    belt_motor.run(-500)
    while not touch_sensor.pressed():
        pass
    belt_motor.stop()
    wait(1000)
    belt_motor.reset_angle(0)

    # Limpa todo o conteúdo do Display.
    brick.display.clear()

    # O escaneamento de um Quadrado Colorido armazena a cor em uma
    # lista. A lista está vazia no início. Ela irá crescer à medida
    # que as cores forem adicionadas.
    color_list = []

    # Este loop escaneia as cores dos objetos. Ele se repete até que
    # 8 objetos sejam escaneados e colocados na rampa. Isso é feito
    # repetindo o loop enquanto o comprimento da lista for menor que 8.
    while len(color_list) < 8:
        # Exibe uma seta que aponta para o Sensor de Cor.
        brick.display.image(ImageFile.RIGHT)

        # Exibe quantos Quadrados Coloridos foram escaneados até agora.
        brick.display.text(len(color_list))

        # Espera até que o Botão Central seja pressionado ou um
        # Quadrado Colorido seja escaneado.
        while True:
            # Armazena "True" se o Botão Central for pressionado ou
            # "False" se não for.
            pressed = Button.CENTER in brick.buttons()
            # Armazena a cor medida pelo Sensor de Cor.
            color = color_sensor.color()
            # Se o Botão Central for pressionado ou uma das cores
            # possíveis for detectada, sai do loop.
            if pressed or color in POSSIBLE_COLORS:
                break

        if pressed:
            # Se o botão foi pressionado, encerra o loop mais cedo.
            # Ele não esperará mais que nenhum Quadrado Colorido seja
            # escaneado e adicionado à rampa.
            break
        else:
            # Caso contrário, uma cor foi escaneada, então ela é
            # adicionada (apendida) à lista.
            brick.sound.beep(1000, 100, 100)
            color_list.append(color)

            # Ele não deve registrar a mesma cor novamente se ainda
            # estiver olhando para o mesmo Quadrado Colorido. Então,
            # antes de continuar, espera até que o sensor não veja mais
            # o Quadrado Colorido.
            while color_sensor.color() in POSSIBLE_COLORS:
                pass
            brick.sound.beep(2000, 100, 100)

            # Exibe uma seta apontando para baixo e espera 2 segundos
            # para dar tempo de deslizar o Quadrado Colorido para a
            # rampa motorizada.
            brick.display.image(ImageFile.BACKWARD)
            wait(2000)

    # Toca um som e exibe uma imagem para indicar que o escaneamento
    # está completo.
    brick.sound.file(SoundFile.READY)
    brick.display.image(ImageFile.EV3)

    # Agora classifica os blocos usando a lista de cores que foram
    # armazenadas. Faz isso percorrendo cada cor na lista.
    for color in color_list:

        # Espera por 1 segundo entre cada ação de classificação.
        wait(1000)

        # Executa o motor da esteira transportadora para a posição
        # que corresponde à cor armazenada.
        if color == Color.BLUE:
            brick.sound.file(SoundFile.BLUE)
            belt_motor.run_target(500, 10)
        elif color == Color.GREEN:
            brick.sound.file(SoundFile.GREEN)
            belt_motor.run_target(500, 132)
        elif color == Color.YELLOW:
            brick.sound.file(SoundFile.YELLOW)
            belt_motor.run_target(500, 360)
        elif color == Color.RED:
            brick.sound.file(SoundFile.RED)
            belt_motor.run_target(500, 530)

        # Agora que a esteira transportadora está na posição correta,
        # ejeta o objeto colorido.
        feed_motor.run_angle(1500, 90)
        feed_motor.run_angle(1500, -90)