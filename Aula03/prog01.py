from datetime import datetime
def ola():
    print("Olá Python")

def hora_certa():
    return datetime.now()

def calculo_imc(altura, peso):
    return peso / (altura * altura)

print(f"Altura: 1.66 | Peso: 80 | IMC: {calculo_imc(1.66, 80):.2f}")