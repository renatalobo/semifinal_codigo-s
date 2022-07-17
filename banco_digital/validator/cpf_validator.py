import re


def valida_cpf_cnpj(cpf):
    return not re.match(r'^([\s\d]+)$', cpf)