import json
import requests

class SPTrans(object):

    def checkAcesso(self):
        message = 'Acesso negado'
        response = requests.get('http://api.olhovivo.sptrans.com.br/v2.1')
        if response.status_code == 200:
            message = 'Acesso ok'
        return message

    def getLinha(self, linha):
        token = '2e8b2a294456f3893544030d8a8386c087e13ce0d105dfc994da5eeef9f3e9e4'
        s = requests.Session()
        response = s.post('http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={token}'.format(token=token))
        print(response.cookies)
        url = 'http://api.olhovivo.sptrans.com.br/v2.1/Posicao/Linha?codigoLinha={linha}'.format(linha=linha)
        response = s.get(url)
        return response

