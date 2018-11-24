import os
import pytesseract as ocr
from os.path import isfile, join
from os import listdir
from PIL import Image

# CAMINHO DAS IMAGENS
DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imgs')
print(DIR_PATH)

# pega todos os arquivos da pasta
only_images = [f for f in listdir(DIR_PATH) if isfile(join(DIR_PATH, f))]
print(only_images)

# vai lendo arquivo por arquivo e mostrando a placa
for imagem in only_images:
    img1 = os.path.join(DIR_PATH,imagem)
    print('Lendo a imagem: {}'.format(img1))

    phrase = ocr.image_to_string(Image.open(img1))
    print('Resultado: {}'.format(phrase))

    print('-'*100)