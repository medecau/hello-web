from bottle import Bottle, jinja2_view as view, static_file, response


app = application = Bottle()

@app.route('/s/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='static/')

@app.route('/')
@view('home.html')
def hello_world():
    #return "Hello World! // %s - %s - %s" % (counter, os.getpid(), time.time())
    return dict(msg='hello')

@app.route('/api/hello')
def hello():
    return '<b>hello</b>'


if __name__ == '__main__':
    #app.run(quiet=True)
    app.run(debug=True, reloader=True)
