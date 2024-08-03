# match case

if __name__ == "__main__":
    
    acesso = input("Informe seu nível de acesso: ")

    match acesso.upper():
        case "USUARIO":
            print("Você possui um nível de acesso básico.")

        case "GESTOR":
            print("Você possui um nível de acesso intermediário.")

        case _:
            print("Você possui acesso total.")