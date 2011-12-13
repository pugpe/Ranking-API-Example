from bottle import route, run, template

@route('/hello')
def hello():
    return template('hello')

run(host='localhost', port=5000)