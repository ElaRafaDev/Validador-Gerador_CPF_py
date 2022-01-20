import random

REGRESSIVOS = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cpf):
    cpf = remover_caracter(cpf)
    try:
        if sequencia(cpf):
            return False
    except:
        return True
    try:
        novo_cpf = calcula_digito(cpf=cpf, digito=1)
        novo_cpf = calcula_digito(cpf=novo_cpf, digito=2)
    except Exception as error:
        return False
    if novo_cpf == cpf:
        return True
    else:
        return False


def remover_caracter(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    return cpf


def sequencia(cpf):
    sequencia = cpf[0] * len(cpf)
    if sequencia == cpf:
        return True
    else:
        return False


def calcula_digito(cpf, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cpf = cpf[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cpf = cpf
    else:
        return None
    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cpf[indice]) * regressivo
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    return '{}{}'.format(novo_cpf, digito)


def gerador_cpf():
    numero = random.randint(100000000, 999999999)
    inicio_cpf = '{}00'.format(numero)
    novo_cpf = calcula_digito(cpf=inicio_cpf, digito=1)
    novo_cpf = calcula_digito(cpf=novo_cpf, digito=2)
    return novo_cpf


def formata(cpf):
    cpf = remover_caracter(cpf)
    formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:12])
    return formatado