from flask import Flask

from project.usecases.apiController import ApiController

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    #app.run()

    url = 'http://api.olhovivo.sptrans.com.br/v2.1'
    apiController = ApiController(url)
    response = apiController.handle()
    print(response)
