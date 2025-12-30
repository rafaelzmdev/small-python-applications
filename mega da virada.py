#Vou usar esse script para gerar uma das três apostas minhas e da minha mãe na mega da virada 2025. Se gerar os seis números vitoriosos, posso dizer que devo todo o dinheiro a minha habilidade de programar; e aos criadores do python.
import random
gen = 0
while gen < 6:
    gen = gen + 1
    lista = random.randint(1, 60)
    print(lista)