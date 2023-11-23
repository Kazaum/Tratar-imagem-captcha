import cv2
from PIL import Image

#Função reponsável por testar diversas tratativas iniciais e ver qual fica mais legível
def TesteMetodos():
    i = 0
    caminho = "bdcaptcha/telanova9.png"
    #Metodos a serem testados
    metodos = [
        cv2.THRESH_BINARY,
        cv2.THRESH_BINARY_INV,
        cv2.THRESH_TRUNC,
        cv2.THRESH_TOZERO,
        cv2.THRESH_TOZERO_INV,
    ]
    #imagem captcha
    imagem = cv2.imread(caminho)

    #transformar a imagem em escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

    #aplicar os metodos a imagem e salvar no dispositivo
    for metodo in metodos:
        caminho_testes = f'TestesMetodo/imagem_tratada_{i}.png'
        i += 1
        _, imagem_tratada = cv2.threshold(imagem_cinza, 127, 255, metodo or cv2.THRESH_OTSU)
        cv2.imwrite(caminho_testes, imagem_tratada)