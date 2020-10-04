import requests

class ApiController(object):

    def __init__(self, url):
        self.url = url

    def handle(self):
        response = requests.get(self.url)

        if response.status_code == 404:
            response.body = 'Not Found'

        if response.status_code == 200:
            response.body = 'Success'

        return response.body

    def verificaAutenticacao(self):
        response = requests.post(self.url)

        if response.status_code == 200:
            if response.text == 'false':
                message = 'Acesso negado - checar token'
            elif response.text == 'true':
                message= 'Sucesso'
        else:
            message = 'Checar url'

        return message
