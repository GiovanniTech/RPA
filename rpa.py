# RPA e Python 
# pyautogui
# Biblioteca para controlar Mouse, Teclado e Tela do Computador com o Python
# (Link: https://pyautogui.readthedocs.io/en/latest/quickstart.html)

# Vamos fazer um exemplo simples aqui, mas repare que isso serve para:

# Qualquer site
# Qualquer programa ou pasta do seu computador
# Qualquer Sistema que você tenha que acessar e automatizar

# Desafio:
# Queremos automatizar o backup de arquivos no sistema
# No nosso exemplo, vamos ter que criar um processo que faça o upload de 1 arquivo no Google Drive de forma automática e rápida

import pyautogui
import time

pyautogui.alert("O Código vai começar, não aperte nada enquanto o código está rodando")
pyautogui.PAUSE = 0.5
# instalar e importar biblioteca do pyautogui >> pip install pyautogui 
# abrir o google drive no meu computador
pyautogui.press('winleft')
pyautogui.write('Google Chrome')
pyautogui.press('enter')
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
time.sleep(2)
pyautogui.press('enter')
#entrar na minha área de trabalho ou local que esteja armazenado o arquivo
pyautogui.hotkey('winleft','d')
time.sleep(1)
# cliquei no arquivo que eu quero fazer o backup e arrastei ele 
pyautogui.moveTo(1879, 90)
pyautogui.mouseDown()
pyautogui.moveTo(1000, 698)
time.sleep(3)
# enquanto eu to arrastando, eu vou mudar para o google drive
pyautogui.hotkey('alt','tab')
# larguei o arquivo no google drive
pyautogui.mouseUp()
# esperar 5 segundos para subir o arquivo
time.sleep(5)

pyautogui.alert('O código acabou de rodar. Pode usar o seu computador de novo')
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
