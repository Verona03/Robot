#importando bibliotecas
import pyautogui as py
import time
   
#condição de repetição infinita
while True:
    try:
        #pressiona os 2 botoes e para por 3 segundos antes de começar a clicar nas abas do BI
        py.hotkey('F5','F11')
        time.sleep(3)


        #clica para maximizar o bi dentro da pagina em f11
        py.click  (x=256, y=200, interval= 1)        
        py.click  (x=256, y=212)
        py.moveTo (x= 0, y = 1000)
        time.sleep(1)
        #clicker com intervalo de tempo entre eles, click em cada aba
        py.click (x=81, y=1071, interval= 32)
        py.click (x=263, y=1071, interval= 30)
        py.click (x=344, y=1071, interval= 30)


        #pressiona os 2 botoes diminuir a pag e ir para outra guia
        py.hotkey('esc', 'F11')
        py.hotkey('ctrl', 'tab')
        time.sleep(1)


    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        time.sleep(5)  # Aguarda 5 segundos antes de tentar novamente


        #Jinx Was Here and Vera Martins too
       
       
#polegada_monitor_usuario/
# ------------------------ * x da cordanada do meu pc
# polegada_meu_monitor
