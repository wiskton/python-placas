# -*- coding: utf-8 -*-
import os
import pytesseract as ocr
from os.path import isfile, join
from os import listdir
from PIL import Image

# CAMINHO DAS IMAGENS
DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imgs')

print('-'*100)

print('Caminho das imagens: {}'.format(DIR_PATH))

print('-'*100)

# pega todos os arquivos da pasta
only_images = [f for f in listdir(DIR_PATH) if isfile(join(DIR_PATH, f))]
print('Todas as fotos da pasta: {}'.format(only_images))

print('-'*100)

# função para gerar texto
def convert_img_to_text(path_imagem):
    return ocr.image_to_string(Image.open(path_imagem))

# vai lendo todas imagens da pasta e convertendo para texto
for imagem in only_images:

    img1 = os.path.join(DIR_PATH,imagem)
    print('Lendo a imagem: {}'.format(img1))

    phrase = convert_img_to_text(img1)
    print('Resultado: {}'.format(phrase))

    print('-'*100)