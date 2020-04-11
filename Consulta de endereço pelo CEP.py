#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import requests
import argparse, sys


parser = argparse.ArgumentParser()
parser.add_argument("--cep", help="entre com um cep válido")
args = parser.parse_args()


def verifyJson(response: str):
    try:
        if response['erro'] == True:
            return False
        return True
    except KeyError: ## True = Sem erros no json | False = Json com problema
        return True

def cep():
    if args.cep:
        cep_int = args.cep
    else:
        print('Bem-vindo ao sistema de consulta de CEP.')
        cep_int = input('Por favor, digite o CEP que você gostaria de procurar na base (ex: 00000000): ')
    responde = requests.get(f'https://viacep.com.br/ws/{cep_int.strip()}/json/')
    # Verifica se a requisiçao HTTP está disponível.
    if responde.status_code != 200 or verifyJson(responde.json()) == False:
        print('Não foi possível acessar o CEP por favor verifique seu número e digite novamente.')
    else:
        # Armazena o dicionario em uma variável
        dados_cep = responde.json()
        dados_bairro = responde.json()
        dados_local = responde.json()
        dados_uf = responde.json()
        # Exibe a chave dentro do dicionário.

        print(f"""
            =========================================
           | CEP: {cep_int},
           | Rua: {dados_cep['logradouro']},        
           | Bairro: {dados_bairro['bairro']},       
           | Cidade: {dados_local['localidade']},    
           | UF: {dados_local['uf']}                 
           ==========================================
           """)
cep() 

valid_cep = False
while valid_cep == False:
    if args.cep:
        sys.exit()
    else:
        again = input('\nDeseja realizar mais uma busca? S ou N: ').lower()
    if again == 's':
        cep()
    else:
        valid_cep = True
        print('Até logo!')
