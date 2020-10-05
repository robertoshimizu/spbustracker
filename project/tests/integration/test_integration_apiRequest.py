import requests
import json

def test_SPTrans_acesso():
    response = requests.get('http://api.olhovivo.sptrans.com.br/v2.1')
    assert response.status_code == 200

def test_SPTrans_autenticacao():
    with open('../../params/sptrans.json') as json_file:
        data = json.load(json_file)
        token = data['key']
    s = requests.Session()
    response = s.post('http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={token}'.format(token=token))
    print(response.cookies)
    assert response.status_code == 200
    assert response.text == 'true'

def test_SPTrans_linha_noauth():
    linha = '1189'
    url = 'http://api.olhovivo.sptrans.com.br/v2.1/Posicao/Linha?codigoLinha={linha}'.format(linha=linha)
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 401

def test_SPTrans_linha_auth():
    with open('../../params/sptrans.json') as json_file:
        data = json.load(json_file)
        token = data['key']
    s = requests.Session()
    response = s.post('http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={token}'.format(token=token))
    print(response.cookies)
    linha = '1189'
    url = 'http://api.olhovivo.sptrans.com.br/v2.1/Posicao/Linha?codigoLinha={linha}'.format(linha=linha)

    response = s.get(url)
    print(response.text)
    assert response.status_code == 200