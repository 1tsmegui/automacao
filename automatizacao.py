# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# passo 3 : importar a base de dados 
# Passo 4 : cadrastrar os produtos 
# Passo 5 : repetir até acabar todos os produtos 


import pyautogui
import time 

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#comando utilizado para esperar o site carregar por 3 segundos para evitar que a automatização 
#vá mais rápcodigo  marca   ido que o site. time.sleep(3)

time.sleep(3)

#passo 2 - fcodigo  marcaacodigo     custo   codigo marcatipo   categoriazer o login no sistema 

pyautogui.click(x=371, y=371)
pyautogui.hotkey("ctrl", "a") 
pyautogui.write("guilherme.dev@gmail.com")
pyautogui.press("tab")
pyautogui.write("gui123")
pyautogui.click(x=661, y=529)
#hotkey comando utilizado para utilizar mais de uma tecla.(copiei para evitar erros)
  
#passo 3 - importar a base de dados 
time.sleep(3) 
import pandas as pd

tabela = pd.read_csv('E:/Programacao/semanapython/automacao/produtos.csv')

print(tabela)

for  linha in tabela.index:
        
    # Passo 4 - cadrastrar um produto 
    #Código 
    pyautogui.click(x=467, y=266)
    codigo = str (tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    #marca 
    pyautogui.press("tab")
    marca = str (tabela.loc[linha ,"marca"])
    pyautogui.write(marca)

    #tipo
    pyautogui.press("tab")
    tipo = str (tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    #categoriacodigo     
     
    pyautogui.press("tab")
    categoria = str (tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)


    #preço unitário
    pyautogui.press("tab")
    preco_unitario = str (tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    #custo
    pyautogui.press("tab")
    custo = str (tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    #obs
    pyautogui.press("tab")
    obs = str (tabela.loc[linha, "obs"])
    if obs != "nam":
        pyautogui.write(obs)

    #clicar no botao de enviar 
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# Passo 5 - Repetir para todos os produtos 



