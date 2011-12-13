from bottle import route, run

@route('/hello')
@route('/hello/:name')
def hello(name='Indigente'):
    return 'Hello %s, how are you?' % name

run(host='localhost', port=5000)