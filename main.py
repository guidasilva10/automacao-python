print('olá mundo')
import pyautogui
pyautogui.FAILSAFE = True
import time
import pandas
link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=475,y=919)
time.sleep(3)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(7)
pyautogui.click(x=675,y=472)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
time.sleep(1)
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:
    pyautogui.click(x=633,y=319)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write("obs")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    pyautogui.click(x=633,y=319)


