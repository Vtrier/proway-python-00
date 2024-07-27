from random import randint
from time import sleep

if __name__ == "__main__":

    heroi = {
        "nome": "Astolfus",
        "att" : 8,
        "def" : 15,
        "hp"  : 30
    }

    monstro = {
        "nome": "Orc",
        "att": 7,
        "def": 13,
        "hp": 20
    }

    batalha_ocorrendo = True
    vencedor = None

    while batalha_ocorrendo:

        print(f"{heroi['nome']} ataca {monstro['nome']}.")
        dado = randint(1,10)

        ataque_heroi = heroi['att'] + dado
        if ataque_heroi > monstro['def']:
            monstro['hp'] = monstro['hp'] - (ataque_heroi -  monstro['def'])

        else:
            print(f"{monstro['nome']} defendeu o ataque")

        if monstro['hp'] <= 0:
            vencedor = heroi
            batalha_ocorrendo = False
            print(vencedor['nome'])
            break

        sleep(1)
# =========================================================
        print(f"{monstro['nome']} ataca {heroi['nome']}.")
        dado = randint(1,10)

        ataque_monstro = monstro['att'] + dado
        if ataque_monstro > heroi['def']:
            heroi['hp'] = heroi['hp'] - (ataque_monstro -  heroi['def'])

        else:
            print(f"{heroi['nome']} defendeu o ataque")

        if heroi['hp'] <= 0:
            vencedor = monstro
            batalha_ocorrendo = False
            print(vencedor['nome'])
            break
        
        print(heroi)
        print(monstro)
        
        sleep(1)