import re
import pyfiglet
#By Laggg & Zenithar_ss
logo = pyfiglet.figlet_format("ChamaCript", font="small")
En = {
'q': '~', 'w': '`', 'e': '|', 'r': '•', 't': '√','y': 'π', 'u': '÷', 'i': '×', 'o': '§', 'p': '∆','a': '£', 's': '¥', 'd': '$', 'f': '¢', 'g': '^','h': '°', 'j': '=', 'k': '{', 'l': '}','z': '%', 'x': '©', 'c': '®', 'v': '™', 'b': '✓','n': '[', 'm': ']',',': '<',  '.': '>'   
}
Des = {valor: clave for clave, valor in En.items()}
patronPermitido = r'^[a-zA-Z\s,\.]*$'

def menu():
    print(logo)

    print("Codificador Chamaco!")
    print("Que desea chamaquear?:")

    while True:
        a = int(input("1-Desencriptar 2-Encriptar 3-Salir: "))
        match a:
            case 1:
                des()
            case 2:
                en()
            case 3:
                print("Programa finalizado")
                break
            case _:
                print("Introduce un valor valido! (1 o 2) ")
                
def en():
    while True:
        print("- ENCRIPTAR -")
        texto = input("Escriba el texto para encriptarlo o presione 0 para volver al menu: ")
        match texto:
            case "0":
                print("Volviendo...")
                break
            case _:
                Encriptado = ""
                if re.match(patronPermitido,texto):
                    for ch in texto.lower():
                        Encriptado += En.get(ch,ch)
                    print(Encriptado)
                    opcion1 = input("Quieres encriptar algo mas (1) o volver al menu(0)?: ")
                    match opcion1:
                        case "1": print("Reiniciando...")
                        case "0":
                            print("Volviendo al menu...")
                            return Encriptado
                        case _:
                            print("Introduzca 1 para seguir o 0 para volver al menu.")  
                else:
                    print("El texto contiene caracteres no validos, solo se permiten los siguientes: a-z, A-Z, comas, puntos y espacios.")
            
def des():
    while True:
        print("- DESENCRIPTAR-")
        texto = input("Escriba el texto para desencriptarlo o escriba 0 para volver al menu: ")
        match texto:
            case "0":
                print("Volviendo...")
                break
            case _:
                Desencriptado = ""
                for ch in texto:
                    validar = any(ch in Des for ch in texto)
                    if not validar and texto.strip():
                        print("Caracteres no validos.")
                    else:
                        Desencriptado += Des.get(ch,ch)
                print(Desencriptado)
                opcion1 = input("Quieres desencriptar algo mas (1) o volver al menu(0)?: ")
                match opcion1:
                    case "1": print("Reiniciando...")
                    case "0":
                        print("Volviendo al menu...")
                        return Desencriptado
                    case _:
                        print("Introduzca 1 para seguir o 0 para volver al menu.")
                                
                        
    
menu()
        
        
        
        
        
        
        
        
        
        
        
        



    
            