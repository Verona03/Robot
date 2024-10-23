ROBO 2 -
import pyautogui as py
import time


#Condição de repetição infinita
while True:
    try:
        #Pressiona os 2 botões e para por 3 segundos
        py.hotkey('F5', 'F11')
        time.sleep(3)


        #Clica para maximizar o BI dentro da página em F11
        exibir = py.locateCenterOnScreen(f"\\10.134.64.76\\c$\\Bot PBI\\exibir_pg_robo.png", confidence=0.7)
        if exibir is not None:
            py.click(exibir.x, exibir.y)
        else:
            print("Imagem 'exibir' não encontrada")
            continue


        max = py.locateCenterOnScreen(f"\\10.134.64.76\\c$\\Bot PBI\\max_pg_robo.png", confidence=0.7)
        if max is not None:
            py.click(max.x, max.y)
        else:
            print("Imagem 'max' não encontrada")
            continue


        time.sleep(8)


        #Clicker com intervalo de tempo entre eles
        py.click(x=81, y=1071, interval=2)
        py.click(x=168, y=1071, interval=10)
        py.click(x=263, y=1071, interval=10)


        #Pressiona os 2 botões e para por 3 segundos
        py.hotkey('esc', 'F11')
        py.moveTo(1919, 511)
        time.sleep(3)


        #############Iniciando a 2° página ###############
       
        #Clica na página do Bya ao lado
        py.click(x=360, y=0)


        py.hotkey('F5', 'F11') #Atualiza e maximiza a página
        time.sleep(3)  #Para por 3 segundos


        #Clica para maximizar o BI dentro da página em F11
        exibir2 = py.locateCenterOnScreen(f"\\10.134.64.76\\c$\\Bot PBI\\exibir_pg_robo.png", confidence=0.7)
        if exibir2 is not None:
            py.click(exibir2.x, exibir2.y)
        else:
            print("Imagem 'exib'ir não encontrada")
            continue


        max2 = py.locateCenterOnScreen(f"\\10.134.64.76\\c$\\Bot PBI\\max_pg_robo.png", confidence=0.7)
        if max2 is not None:
            py.click(max.x, max.y)
        else:
            print("Imagem 'max' não encontrada")
            continue


        time.sleep(8)


        #Clicker com intervalo de tempo entre eles
        py.click(x=81, y=1071, interval=2)
        py.click(x=168, y=1071, interval=10)
        py.click(x=263, y=1071, interval=10)
       
        py.hotkey('esc', 'F11')
        py.click(x=110, y=0) #Clica na página ao lado e continua o fluxo infinito


    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        time.sleep(5)  #Aguarda 5 segundos antes de tentar novamente
