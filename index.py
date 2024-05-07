import pyautogui
import time


pyautogui.press("win")
pyautogui.write("chrome")  

pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://mattshoes-cadastro.vercel.app/")
pyautogui.press("enter")
time.sleep(3)



import pandas as pd

tabela = pd.read_csv("produtos.csv")


for linha in tabela.index: 
  pyautogui.click(774, 379)
  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(str(codigo))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "marca"]))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "tipo"]))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")

  obs = str(tabela.loc[linha, "obs"])
  if obs != "nan":
    pyautogui.write(obs)
  pyautogui.press("tab")

  pyautogui.press("enter")
  pyautogui.scroll(5000)
