from flask import Flask

from project.usecases.apiController import ApiController
from project.usecases.getLinha import SPTrans

app = Flask(__name__)


@app.route('/')
def hello_world():

    api = SPTrans()
    response = api.getLinha('1189')
    print(response.status_code)
    return str(response.text)


if __name__ == '__main__':
    app.run()


