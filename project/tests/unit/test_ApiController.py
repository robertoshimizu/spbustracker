from project.usecases.apiController import ApiController
import requests

def test_criar_apiController():
    url = 'http://test.com'
    apiController = ApiController(url)
    assert apiController is not None

def test_url(requests_mock):
    requests_mock.get('http://test.com', text = 'data')
    assert ('data' == requests.get('http://test.com').text)

def test_apiController_success_response(requests_mock):
    url = 'http://test.com'
    requests_mock.get(url, status_code = 200)
    response = ApiController(url).handle()
    assert ('Success' == response)

def test_apiController_notFound_response(requests_mock):
    url = 'http://test.com'
    requests_mock.get(url, status_code = 404)
    response = ApiController(url).handle()
    assert ('Not Found' == response)

def test_apiController_authentication_success(requests_mock):
    url = 'http://test.com'
    requests_mock.post(url, text='true')
    response = ApiController(url).verificaAutenticacao()
    assert ('Sucesso' == response)

def test_apiController_authentication_failure(requests_mock):
    url = 'http://test.com'
    requests_mock.post(url, text='false')
    response = ApiController(url).verificaAutenticacao()
    assert ('Acesso negado - checar token' == response)