from colorama import init, Fore, Style
init()
import subprocess
import os
def mostrar_bienvenida():
    print("=" * 40)
    print("   67_OS")
    print("   by: Er Softwares")
    print(" Para ver los comandos escribe: help")
    print("=" * 40)
def mostrar_imagen():
    print(Fore.GREEN + r"""
       .ooo    ooooooooo        .oooooo.    .oooooo..o 
  .88'     d"""""""8'       d8P'  `Y8b  d8P'    `Y8 
 d88'            .8'       888      888 Y88bo.      
d888P"Ybo.      .8'        888      888  `"Y8888o.  
Y88[   ]88     .8'         888      888      `"Y88b 
`Y88   88P    .8'          `88b    d88' oo     .d8P 
 `88bod8'    .8'            `Y8bood8P'  8""88888P'  
      
    """ + Style.RESET_ALL)
def shell():
    while True:
        comando = input("> ").strip()

        if comando == "help":
            print("Comandos disponibles:")
            print(" help  - muestra esta ayuda")
            print(" cls   - limpia la pantalla")
            print(" echo  - repite texto")
            print(" exit  - salir")
            print(" run   - ejecutar un programa, debes añadir la ruta completa ej: run C:\Windows\System32\notepad.exe")

        elif comando == "cls":
            print("\n" * 50)

        elif comando.startswith("echo "):
            print(comando[5:])

        elif comando == "exit":
            print("Apagando 67 OS...")
            break

        elif comando.lower().startswith("run "):
            archivo = comando[4:].strip()

            # quitar comillas si vienen del usuario
            if archivo.startswith('"') and archivo.endswith('"'):
                archivo = archivo[1:-1]

            print(f"Ejecutando {archivo}...")

            try:
                subprocess.Popen(
                    f'cmd /c start "" "{archivo}"',
                    shell=True
                )
            except Exception as e:
                print("Error al ejecutar:", e)
                
mostrar_bienvenida()
mostrar_imagen()
shell()