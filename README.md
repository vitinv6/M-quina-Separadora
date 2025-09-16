# Robô Classificador de Cores EV3

Este projeto consiste em um robô construído com o kit LEGO® MINDSTORMS® EV3, programado em MicroPython, para classificar blocos de cores de forma autônoma. O robô utiliza sensores e motores para identificar, separar e ejetar blocos de cores específicas em compartimentos designados.

## Integrantes do Grupo

* Bryan Belum
* Guilherme Marinho
* Jhoysell Chavarria
* Marcio Zulin
* Vitor Venturi

## Funcionalidades do Robô

* **Inicialização Automática:** Os motores da esteira e da rampa são automaticamente calibrados para suas posições de início ao ligar o robô.
* **Escaneamento de Cores:** Utiliza um Sensor de Cor para identificar blocos nas cores vermelho, verde, azul e amarelo.
* **Armazenamento de Dados:** Armazena a sequência de cores escaneadas em uma lista interna.
* **Classificação e Ejeção:** Move a esteira para a posição correta e utiliza um motor para ejetar cada bloco em seu respectivo compartimento de cor.
* **Interface Simples:** Usa a tela do EV3 para exibir instruções e o número de blocos já escaneados.
* **Loop Infinito:** O programa é executado em um loop contínuo, permitindo que o robô classifique conjuntos de blocos repetidamente.

## Estrutura do Código

O código-fonte (`cod_robo.py`) é escrito em MicroPython para o kit EV3 e está dividido nas seguintes seções:

* **Importações:** Bibliotecas necessárias para controlar os motores, sensores e a tela do EV3.
* **Configurações:** Definição de constantes e inicialização dos motores e sensores.
* **Loop Principal (`while True`):** A lógica principal do programa, que engloba as três etapas:
    1.  **Inicialização dos Motores:** Retorna os motores à posição de partida.
    2.  **Escaneamento de Blocos:** Loop para ler até 8 blocos de cores.
    3.  **Classificação dos Blocos:** Itera pela lista de cores para mover e ejetar cada bloco.

## Requisitos de Hardware

Para reproduzir este projeto, você precisará dos seguintes componentes do kit LEGO® MINDSTORMS® EV3:

* 1x Bloco EV3
* 1x Motor Grande (para a esteira)
* 1x Motor Médio (para a rampa)
* 1x Sensor de Toque
* 1x Sensor de Cor
* Blocos LEGO para montar a estrutura do robô (esteira, rampa, etc.)
* 4x blocos de cores (vermelho, verde, azul, amarelo)

## Como Rodar o Código

1.  Conecte o bloco EV3 ao seu computador.
2.  Transfira o arquivo `cod_robo.py` para o bloco EV3 usando a interface de desenvolvimento do MicroPython.
3.  Execute o programa a partir do menu do EV3.

## Contribuições

Este projeto foi desenvolvido como parte de um trabalho em grupo. Sugestões de melhorias e novas funcionalidades são bem-vindas. Sinta-se à vontade para abrir uma *issue* ou um *pull request*.
