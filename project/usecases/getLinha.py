import json
import requests
# import os

class SPTrans(object):

    def checkAcesso(self):
        message = 'Acesso negado'
        response = requests.get('http://api.olhovivo.sptrans.com.br/v2.1')
        if response.status_code == 200:
            message = 'Acesso ok'
        return message

    def getLinha(self, linha):
        # currentDirectory = os.getcwd()
        with open('./project/params/sptrans.json') as json_file:
            data = json.load(json_file)
            token = data['key']
        s = requests.Session()
        response = s.post('http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={token}'.format(token=token))
        # print(response.cookies)
        url = 'http://api.olhovivo.sptrans.com.br/v2.1/Posicao/Linha?codigoLinha={linha}'.format(linha=linha)
        response = s.get(url)
        return response

