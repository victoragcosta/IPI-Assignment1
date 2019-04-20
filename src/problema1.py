import cv2
import numpy as np

# Escreve o número de 8 bits em binário (utilizado para debug)
def print_binario(num):
  for i in range(7,-1,-1):
    print((num//(2**i))%2,end="")
  print()

# Conta quantos pixels de cada nível tem (utilizado para debug)
def histograma(img):
  niveis = {}
  for item in tratado.flat:
    try:
      niveis[item]+=1
    except:
      niveis[item] = 0
  return niveis

# Questão 1
def imscaledepth(img, n_bits, scale):

  # Crio uma cópia para poder modificar sem alterar a original
  newimg1 = img.copy()

  # Adiciono uma dimensão caso seja escala de cinza para generalizar
  # o código
  if len(img.shape) == 2:
    newimg1 = newimg1[:,:,np.newaxis]

  # Pego as dimensões da imagem e quantidade de canais
  height, width, channels = newimg1.shape

  # Crio a nova imagem escalonada preenchida com 0s
  newimg2 = np.zeros((int(height*scale),int(width*scale),channels), dtype=np.uint8)

  # Processamento caso seja para reduzir a escala
  if scale <= 1:
    # fac representa quantas vezes a original é maior que a nova
    fac = 1/scale
    # Percorro toda a matriz nova
    for l in range(newimg2.shape[0]):
      for c in range(newimg2.shape[1]):
        # Pego uma matriz fac por fac e
        matrix = newimg1[int(l*fac):int((l+1)*fac),int(c*fac):int((c+1)*fac),:]
        # Para cada canal faço a soma de seus elementos
        elements_sum = np.sum(matrix,axis=(0,1),dtype=np.int32)
        # Para fazer a media divido a soma pelas dimensões obtidas
        average = elements_sum/(matrix.shape[0]*matrix.shape[1])
        # Atribuo a média de cada canal a seu respectivo novo canal
        newimg2[l:l+1,c:c+1,:] = average
  else:
    # fac representa quantas vezes a nova é maior que a original
    fac = scale
    # Percorro toda a matriz original
    for l in range(height):
      for c in range(width):
        # Para cada matriz de fac por fac atribuo os valores de
        # um dos pixels da matriz original
        newimg2[int(l*fac):int((l+1)*fac),int(c*fac):int((c+1)*fac),:] = newimg1[l:l+1,c:c+1,:]

  # Divido por 2 números de bits descartados vezes
  # para retirar os bits menos significativos e
  # alinhar a direita
  factor = 2**(8-n_bits)
  newimg2 = newimg2 // factor

  # Converto a imagem de n_bits para 2^n_bits de níveis
  # em uma imagem 8 bits (multiplica por um fator que faz
  # 0 virar 0 e o maior valor para n_bits 255, o meio escalona
  # proporcional)
  multiplier = 255//(2**n_bits - 1)
  newimg2 = newimg2 * multiplier

  # Como adicionei uma dimensão às imagens escala de cinza
  # vou retirá-las
  if len(img.shape) == 2:
    newimg2 = np.squeeze(newimg2, axis=2)

  return newimg2

#================ Main ================#

img = cv2.imread("img/im1.jpg")
cv2.imshow("Original", img)

img_tratado = imscaledepth(img, 5, 0.5)
cv2.imshow("Colorida n_bits=5 scale=0.5", img_tratado)
#cv2.imwrite("img/resultado/im1_color_5bits_0.5.jpg", img_tratado)

img_tratado2 = imscaledepth(img, 3, 1.75)
cv2.imshow("Colorida n_bits=3 scale=1.75", img_tratado2)
#cv2.imwrite("img/resultado/im1_color_3bits_1.75.jpg", img_tratado2)

cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Escala de Cinza", gray)
#cv2.imwrite("img/im1_cinza.jpg", gray)

gray_tratado = imscaledepth(gray, 5, 0.5)
cv2.imshow("Cinza n_bits=5 scale=0.5", gray_tratado)
#cv2.imwrite("img/resultado/im1_cinza_5bits_0.5.jpg", gray_tratado)

gray_tratado2 = imscaledepth(gray, 3, 1.75)
cv2.imshow("Cinza n_bits=3 scale=1.75", gray_tratado2)
#cv2.imwrite("img/resultado/im1_cinza_3bits_1.75.jpg", gray_tratado2)

cv2.waitKey(0)
cv2.destroyAllWindows()
