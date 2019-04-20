import numpy as np
import cv2

# Função que converte uma imagem BGR para Escala de Cinza
def convert2grayscale(img):
  # Pega as dimensões
  height, width, channels = img.shape
  # Crio nova matriz em escala de cinza
  gray = np.zeros((height, width), dtype=np.uint8)

  b = img[:,:,0:1].squeeze(axis=2)
  g = img[:,:,1:2].squeeze(axis=2)
  r = img[:,:,2:3].squeeze(axis=2)

  gray[:,:] = 0.299*r + 0.587*g + 0.114*b

  return gray

# Função faz equalização de histograma de uma imagem
def equalization(img):
  # Calcula histograma
  hist = [0 for i in range(256)]
  for item in img.flat:
    hist[item] += 1

  # Normaliza histograma
  height, width = img.shape
  n = height*width
  hist_norm = list(map(lambda item:item/n, hist))

  # Calcula probabilidade acumulada
  cdf = [0 for i in range(256)]
  for i in range(256):
    if i == 0:
      cdf[i] = hist_norm[i]
    else:
      cdf[i] = cdf[i-1] + hist_norm[i]

  # Calcula probabilidade acumulada vezes níveis-1 (255)
  cdf_mult = list(map(lambda item:round(item*255), cdf))

  # Cria nova imagem equalizada
  heq = (np.vectorize(lambda pixel: cdf_mult[pixel])(img)).astype(np.uint8)

  return heq

# Função que dada uma posição (x,y) retorna todos os 8 vizinhos
def get_neighbors_pos(pos):
  neighbors = []
  for i in range(-1,2):
    for j in range(-1,2):
      neighbors.append((pos[0]+i,pos[1]+j))
  return neighbors

# Função que dado uma imagem desenha um caminho sobre ela
def drawPath(img, path, size=1):
  newimg = img.copy()
  # Desenha caminho
  for p in path:
    newimg[p[0]+1-size:p[0]+size,p[1]+1-size:p[1]+size] = 0
  return newimg

# Função que gera um vetor com o caminho de menor esforço
def go2destination(img, start, stop):
  # Inicializo posição
  pos = start
  # Inicializo caminho
  path = [start]
  # Procuro caminho até chegar no ponto esperado
  while pos != stop:
    # Pego os 8 vizinhos ao redor de pos
    near = get_neighbors_pos(pos)

    # Escolho os 3 candidatos mais próximos do destino
    # utilizando dx^2+dy^2, pois tirar raiz quadrada não
    # melhora a ordenação e só gasta processamento
    candidates = sorted(near, key=lambda item:(item[0]-stop[0])**2+(item[1]-stop[1])**2)[0:3]

    # Pego os valores de brilho, ordeno pelo brilho e escolho o primeiro
    chosen = sorted([(img.item(p), p) for p in candidates], key=lambda item:item[0])[0]

    # Atualizo a posição
    pos = chosen[1]

    # Adiciono posição no caminho
    path.append(pos)

  return path

#================ Main ================#

MRGB = cv2.imread("img/Mars.bmp")
#cv2.imshow("Original", MRGB)
cv2.imshow("Original", cv2.resize(MRGB,None, fx=0.5, fy=0.5))
cv2.waitKey(0)

MGray = convert2grayscale(MRGB)
#cv2.imshow("Escala de Cinza", MGray)
cv2.imshow("Escala de Cinza", cv2.resize(MGray,None, fx=0.5, fy=0.5))
cv2.imwrite("img/resultado/Mars_cinza.jpg", MGray)
cv2.imwrite("img/resultado/Mars_cinza.bmp", MGray)
cv2.waitKey(0)

MHeq = equalization(MGray)
#cv2.imshow("Equalizada", MHeq)
cv2.imshow("Equalizada", cv2.resize(MHeq,None, fx=0.5, fy=0.5))
cv2.imwrite("img/resultado/Mars_equalizada.jpg", MHeq)
cv2.imwrite("img/resultado/Mars_equalizada.bmp", MHeq)
cv2.waitKey(0)

start = (260,415)
stop = (815,1000)

path = go2destination(MHeq, start, stop)
MPath = drawPath(MRGB, path, size=1)
#cv2.imshow("Caminho", MPath)
cv2.imshow("Caminho", cv2.resize(MPath,None, fx=0.5, fy=0.5))
cv2.imwrite("img/resultado/Mars_caminho.jpg", MPath)
cv2.imwrite("img/resultado/Mars_caminho.bmp", MPath)
cv2.waitKey(0)

cv2.destroyAllWindows()
