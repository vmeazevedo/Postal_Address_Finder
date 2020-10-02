#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import requests
print('\nBem-vindo ao sistema de consulta de CEP.')


def verifyJson(response: str):
    try:
        if response['erro'] == True:
            return False
        return True
    except KeyError: ## True = Sem erros no json | False = Json com problema
        return True

def cep():
    cep_int = input('Por favor, digite o CEP que você gostaria de procurar na base (ex: 00000000): ')
    responde = requests.get(f'https://viacep.com.br/ws/{cep_int.strip()}/json/')
    # Verifica se a requisiçao HTTP está disponível.
    if responde.status_code != 200 or verifyJson(responde.json()) == False:
        print('\033[31mNão foi possível acessar o CEP por favor verifique seu número e digite novamente.\033[0;0m')
    else:
        # Armazena o dicionario em uma variável
        cep_info = responde.json()
        # Exibe a chave dentro do dicionário.

        print(f"""
            =========================================
           | CEP: {cep_int},        
           | Rua: {cep_info.get('logradouro', 'Não encontrado')},        
           | Bairro: {cep_info.get('bairro', 'Não encontrado')},       
           | Cidade: {cep_info.get('localidade', 'Não encontrado')},    
           | UF: {cep_info.get('uf', 'Não encontrado')}                 
           ==========================================
           """)
cep() 

valid_cep = False
while valid_cep == False:   
    again = input('\nDeseja realizar mais uma busca? S ou N: ').lower()
    if again == 's':
        cep()
    else:
        valid_cep = True
        print('Até logo!')
