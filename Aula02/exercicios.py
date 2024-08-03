if __name__ == "__main__":
    from random import randint
    
    def ex01():
        numero = int(input("Informe um número: "))

        if numero < 1:
            print("O numero deve ser maior ou igual a 1.")

        else:
            contador = 1
            soma = 0

            while contador <= numero:
                soma = soma + contador
                contador += 1

            print(f"A soma de 1 até {numero} é igual a {soma}")

    def ex02():
        lista_numeros = []
        
        while True:
            numero = int(input("Digite um número: "))

            if numero == 0:
                break
        
            lista_numeros.append(numero)

        lista_quadrados = [numero * numero for numero in lista_numeros]

        print(f"Lista dos quadrados: {lista_quadrados}")

    def ex03():
        numeros_pares = []
        numeros_impares = []

        for _ in range(100):

            numero_randomico = randint(1,100)

            if numero_randomico % 2 == 0:
                numeros_pares.append(numero_randomico)
            
            else:
                numeros_impares.append(numero_randomico)

        print(f"Lista de números pares: {numeros_pares}.")
        print(f"Tamanho: {len(numeros_pares)}.")
        print("*"*30)
        print(f"Lista de números ímpares: {numeros_impares}.")
        print(f"Tamanho: {len(numeros_impares)}.")

    def ex04():
        lista = [4, 7, 10, 24]

        saida = ""

        for numero in lista:
            saida = f"{saida}{numero}"
        
        print(f"Saída: {saida}")

    def ex05():
        lista_randomicos = [randint(0,50) for _ in range(50)]

        print(f"Lista: {lista_randomicos}")
        print(f"Maior número da lista: {max(lista_randomicos)}.")
        print(f"Menor número da lista: {min(lista_randomicos)}.")

    def ex06():
        for numero in range(1, 6):
            print("#"*numero)

    def ex07():
        qtd_masculino = 0
        qtd_feminino = 0
        soma_idade = 0
        media_idade = 0
        lista_usuarios = []
        qtd_usuarios = 5

        for _ in range(qtd_usuarios):
            nome = input("Informe o seu nome: ")
            idade = int(input("Indforme a sua idade: "))
            sexo = input("Informe o seu sexo (M ou F): ").upper()
            print('-'*50)

            if idade <= 0:
                print("Informe uma idade válida.")
                break

            elif sexo not in ["M", "F"]:
                print("Você deve informar 'M' ou 'F' para sexo.")
                break

            soma_idade = soma_idade + idade
            if sexo == "M":
                qtd_masculino += 1

            else:
                qtd_feminino += 1

            lista_usuarios.append({
                "nome": nome,
                "idade": idade,
                "sexo": sexo
            })
        else:
            media_idade = soma_idade / qtd_usuarios

            for usuario in lista_usuarios:
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']}")
                print(f"Sexo: {usuario['sexo']}")
                print()

            print("Quantidade de ")

    def ex08():
        pass

ex08()