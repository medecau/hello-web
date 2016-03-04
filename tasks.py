from bottle import Bottle, debug
from bottle import request, response
from logging import log
from models import Counter
from google.appengine.api import taskqueue


app = application = Bottle()
debug(True)

@app.route('/tasks/hourly')
def hourly():
    return 'ok'

@app.route('/tasks/count', ['POST'])
def count():
    try:
        counter = Counter.query(Counter.name == 'hello').fetch()[0]
    except IndexError:
        log.info('New counter.')
        counter = Counter(name='hello', count=0)
    counter.count += 1
    counter.put()
    return


if __name__ == '__main__':
    #app.run(quiet=True)
    app.run(debug=True, reloader=True)
