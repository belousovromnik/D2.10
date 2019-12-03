import sentry_sdk

from bottle import Bottle, request, template
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://a67218672e6246d88f20e78e880acf24@sentry.io/1824508",
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/')
def index():
    name = 'Гость'
    return 'Заглавная страница!'


@app.route('/success')
def index():
    return 'Страница, которая возвращает положительный ответ!'


@app.route('/fail')
def index():
    raise RuntimeError("There is an error111!")
    return


app.run(host='localhost', port=8090)
