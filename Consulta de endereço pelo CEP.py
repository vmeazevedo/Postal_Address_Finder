import requests

print('\nBem-vindo ao sistema de consulta de CEP.')

def cep():
    cep_int = input('Por favor, digite o CEP que você gostaria de procurar na base (ex: 00000000): ')
    responde = requests.get('https://viacep.com.br/ws/' + cep_int + '/json/')
    # Verifica se a requisiçao HTTP está disponível.
    if responde.status_code != 200:
        print('Não foi possível acessar o CEP por favor verifique seu número e digite novamente.')
    else:
        # Armazena o dicionario em uma variável
        dados_cep = responde.json()
        dados_bairro = responde.json()
        dados_local = responde.json()
        dados_uf = responde.json()
        # Exibe a chave dentro do dicionário.
        print('Rua: '+dados_cep['logradouro'],','+ dados_bairro['bairro'],','+ dados_local['localidade'],','+dados_uf['uf'],'.')
        
cep()

valid_cep = False
while valid_cep == False:   
    again = input('\nDeseja realizar mais uma busca? S ou N: ').lower()
    if again == 's':
        cep()
    else:
        valid_cep = True
        print('Até logo!') 