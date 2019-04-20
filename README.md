# Trabalho 1 IPI
Primeiro trabalho da disciplina de Introdução ao Processamento de Imagens da
Universidade de Brasília

Matricula | Nome
----------|-------------------------
160019311 | Victor André Gris Costa

## Problemas

### Questão 1
Faça uma FUNÇÃO chamada “im_chscaledepth”. Esta função deve receber 3 argumentos.
O primeiro é uma imagem colorida ou monocromática, os outros dois argumentos são
números. O primeiro é um número inteiro e o segundo um número fracionário. O primeiro
número representa a quantidade de bits que a imagem de saída deve ter, este número deve
variar de 1 a 8. A imagem de saída então deve ter níveis de brilho (ou cor) de acordo com a
quantidade de bits (8 bits – 256 níveis, 7 bits – 128 níveis, etc. Não é necessário a mudança na
quantidade de bits do pixel, somente adaptar os níveis de brilho ou cor). O segundo valor indica o
fator para redimensionar a imagem, um valor de 0.5 significa que a imagem deve ficar com
metade das linhas e colunas, um valor de 2.0 significa que deve ficar com o dobro. Para
aumentar a quantidade de pixels, sua função deve simplesmente repetir filas e colunas. Não é
permitido utilizar funções prontas do Matlab ou OpenCV para trocar tamanho ou quantidade
de níveis de cinza da imagem.

### Questão 2
Suponha que você é parte de um tme de astronautas que faz parte da primeira missão para
Marte. Sua missão é de obter informação, e obter um material de estudo do solo de marte de
um local específico. Você possui um mapa RGB de parte da superfície de Marte. Você quer
chegar no local de retirada do material de estudo o mais rápido possível de forma de gastar a
menor quantidade de energia do seu veículo.
Assim, faço o seguinte:

1. Carregue a imagem da superfície de Marte: Mars.bmp, chame a imagem de MRGB
2. Escreva uma função para converter MRGB para sua versão monocromática MGray (y,i)
(não é permitido utilizar função pronta do Matlab ou OpenCV).
3. Faça a equalização de histograma gerando a imagem MHeq. Após estudos você verificou que
o brilho equalizado da imagem é proporcional a dificuldade do terreno que deve ser percorrido.
Nesta parte é permitido o uso de função pronta do Matlab ou OpenCV.
4. Selecione MHeq(260,415) como o lugar onde você esta e MHeq(815,1000) como o ponto
onde você quer ir para acessar o material de estudo.

Dado uma posição qualquer no mapa a próxima posição do caminho que consume menos
energia é dado por: (1) o valor dos pixels vizinhos; e (2) a distância entre os pixels vizinhos
e o destino final. Primeiro calcule a distância Euclidiana de todos os 8 vizinhos do pixel atual
para o destino final. Depois, selecione os 3 pixels com menor distância como possíveis candidatos.
Entre estes candidatos o pixel com menor valor de brilho representa a próxima posição do
caminho.

## Bibliotecas usadas
* Utilizou-se [Python versão 3.7.3](https://www.python.org/downloads/release/python-373/)
* A instalação das bibliotecas pode ser feita através do comando
`pip3 install <nome da biblioteca>`

Nome          | Versão
--------------|----------
numpy         | 1.16.2
opencv-python | 4.0.0.21


## Modo de uso
### Problema 1
1. Navegue seu shell para a pasta raiz deste projeto (onde o README.md está)
2. Execute com um desses comandos dependendo do seu sistema e configurações:
  * `python src/problema1.py`
  * `python3 src/problema1.py`
  * `python3.7 src/problema1.py`

### Problema 2
1. Navegue seu shell para a pasta raiz deste projeto (onde o README.md está)
2. Execute com um desses comandos dependendo do seu sistema e configurações:
  * `python src/problema2.py`
  * `python3 src/problema2.py`
  * `python3.7 src/problema2.py`
