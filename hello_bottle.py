import uuid
from bottle import Bottle, debug
from bottle import request, response
from bottle import jinja2_view as view, static_file
import logging as log
from models import Counter

app = application = Bottle()
secret = 'secret'
debug(True)

@app.route('/s/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='static/')

@app.route('/')
@view('home.html')
def hello_world():
    sid = request.get_cookie('msg', secret=secret)
    if sid is None:
        sid = uuid.uuid4()
        log.info('New session: %s' % sid)
        response.set_cookie('msg', 'hello', secret=secret)
    return dict(msg='hello')

@app.route('/api/hello')
def hello():
    msg = request.get_cookie('msg', secret=secret)
    if msg is None:
        log.info('Api request without sid.')
    try:
        counter = Counter.query(Counter.name == 'hello').fetch()[0]
    except IndexError:
        log.info('New counter.')
        counter = Counter(name='hello', count=0)
    counter.count += 1
    counter.put()
    return '%s - %s' % (msg, str(counter.count))

    return str(counter)


if __name__ == '__main__':
    #app.run(quiet=True)
    app.run(debug=True, reloader=True)
