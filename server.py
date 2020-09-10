#!/usr/bin/env python3

from bottle import route, run,request

@route('/')
def index():
    name = request.query.name
    age = request.query.age
    apellido = request.query.apellido
    if name and age:
        return f'{name} tiene {age} '
    else:
        return "Hola que tal"


if __name__ == "__main__":
    run(host='0.0.0.0', port=80, debug=True,reloader=True)
