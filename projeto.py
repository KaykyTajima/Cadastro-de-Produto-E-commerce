'''
#Passo a passo do projeto:
#1 Entrar na aba de anúncios do Ml
#2 Procurar o SKU de um produto
#3 Entrar no anúncio e copiar o link
#4 ir no excell e colar o link 
#5 repetir o processo para todos os produtos
 '''
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 2



#1 Entrar na aba de anúncios do Ml

pyautogui.click(x=634, y=1067) # chorome
pyautogui.click(x=156, y=96) # ml
time.sleep(2)
pyautogui.click(x=1237, y=204) #logo da loja
time.sleep(2)
pyautogui.click(x=1145, y=664) # anuncios
time.sleep(3)

#2 Procurar o SKU de um produto na base
tabela = pd.read_csv('estoque.csv',encoding='latin-1')



for i in tabela.index:
    pyautogui.click(x=549, y=494)
    pyautogui.write(str((tabela.loc[i,'SKU'])))
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.scroll(150)
    pyautogui.click(x=581, y=656)
    #3 Entrar no anúncio e copiar o link
    pyautogui.click(x=480, y=56)
    link = pyautogui.hotkey('ctrl','c')
    #4 ir no excell e colar o link 
    tabela[i]["Link"] = link






