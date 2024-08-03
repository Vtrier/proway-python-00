if __name__ == "__main__" :
    # curso = "Pyton"

#     for letra in curso:
#         print(letra, end='-')

    from random import randint

#     lista_de_numeros = [1, 2, 3, 4, 5, 6]
#     lista_de_numeros_ao_quadrado = []

# for numero in lista_de_numeros:
#     lista_de_numeros_ao_quadrado.append(numero * numero)

#     print(lista_de_numeros_ao_quadrado)

lista_randomicos = []

# Utilizando o método append
#for numero in range(1, 101):
  #  lista_randomicos.append(randint(1, 100))

#Utilizando list-comprehension
# lista_randomicos = [randint(1, 100) for _ in range(1, 101)]

# print(lista_randomicos)

lista = [1, 1, 1, 0, 1]

for resultado in lista:
    if resultado == 0:
        print("Nem todos os resultados obtiveram êxito.")
        break
else:
    print("Todos os resultados com êxito.")