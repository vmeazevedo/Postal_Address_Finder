# Made by: Vinícius Azevedo
# Instagram: instagram.com/v.mazevedo
# Twitter: twitter.com/vmeazevedo

import requests
import os


class PostalAddress:
    BASE_URL = 'https://viacep.com.br/ws/{}/json/'

    def __init__(self):
        self.is_zip_code_validated: bool = False
        self.has_response_error: bool = False
        self.response = None
        self.response_json: dict = {}
        self.expected_keys = {'cep': 'CEP',
                              'logradouro': 'Rua',
                              'bairro': "Bairro",
                              'localidade': 'Cidade',
                              'uf': 'UF'}

    def validate_response_error(self, response: dict):
        try:
            self.has_response_error = response['erro']
        except KeyError:
            self.has_response_error = False

    def get_zip_code(self):
        print('\033[1;15m Bem-vindo ao sistema de consulta de CEP \033[0;0m')

        try:
            zip_code = input('Por favor, digite o CEP (ex: 12345678): ')
            self.response = requests.get(self.BASE_URL.format(zip_code.strip()))
            self.response_json: dict = self.response.json()
            self.validate_response_error(self.response_json)
            if self.response.status_code != 200 or self.has_response_error:
                raise TypeError
        except Exception:
            print('\033[31mCEP inválido! por favor, verifique seu número e digite novamente.\033[0;0m')

        for key in self.response_json:
            if self.expected_keys.get(key):
                print(f'\033[1;32m {self.expected_keys[key]}: {self.response_json[key]} \033[0;0m')

    def remake(self):
        while not self.is_zip_code_validated:
            again = input('Deseja realizar mais uma busca? S / N: ').lower()
            if again == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.get_zip_code()
            else:
                self.is_zip_code_validated = True
                print('Até logo!')
