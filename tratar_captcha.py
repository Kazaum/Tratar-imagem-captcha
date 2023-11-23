import cv2
from PIL import Image
from teste_metodo import TesteMetodos

#Função responsável por transformar a imagem mais legível dentre os testes em um Captcha tratado (preto e branco)
def TratarCaptcha():
    caminho_final = "ImagemTratada/imagem_final.png"
    caminho_imagem = "TestesMetodo/imagem_tratada_3.png"
    #Recebe a imagem mais legível e cria uma cópia completamente branca
    imagem = Image.open(caminho_imagem)
    imagem = imagem.convert("L")
    imagem2 = Image.new("L", imagem.size, 255)

    #Recria a versão mais legível de uma forma totalmente preta e branca deixando mais fácil a leitura para o computador
    for x in range(imagem.size[1]):
        for y in range(imagem.size[0]):
            cor_pixel = imagem.getpixel((y, x))
            if cor_pixel < 115:
                imagem2.putpixel((y, x), 0)
    #Salva a imagem tratada no dispositivo            
    imagem2.save(caminho_final)

#Chamar funções
TesteMetodos()
TratarCaptcha()