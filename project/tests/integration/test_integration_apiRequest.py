import requests
import json

def test_SPTrans_acesso():
    response = requests.get('http://api.olhovivo.sptrans.com.br/v2.1')
    assert response.status_code == 200

def test_SPTrans_autenticacao():
    with open('../../params/sptrans.json') as json_file:
        data = json.load(json_file)
        token = data['key']
    response = requests.post('http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={token}'.format(token=token))
    assert response.status_code == 200
    assert response.text == 'true'