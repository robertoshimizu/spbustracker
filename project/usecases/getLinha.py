import json
import requests
from pathlib import Path

class SPTrans(object):

    def getApiToken(self):
        p = Path('.')
        lata = list(p.glob('**/params.json'))
        q = lata[0]
        with q.open() as json_file:
            data = json.load(json_file)
            token = data['sptrans']
        return token

    def checkAcesso(self):
        message = 'Acesso negado'
        response = requests.get('http://api.olhovivo.sptrans.com.br/v2.1')
        if response.status_code == 200:
            message = 'Acesso ok'
        return message

    def getLinha(self, linha):
        token = self.getApiToken()
        s = requests.Session()
        response = s.post('http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={token}'.format(token=token))
        #print(response.cookies)
        url = 'http://api.olhovivo.sptrans.com.br/v2.1/Posicao/Linha?codigoLinha={linha}'.format(linha=linha)
        response = s.get(url)
        return response

    def getAllLinhas(self):
        token = self.getApiToken()
        s = requests.Session()
        response = s.post('http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={token}'.format(token=token))
        # print(response.cookies)
        url = 'http://api.olhovivo.sptrans.com.br/v2.1/Posicao'
        response = s.get(url)
        return response

