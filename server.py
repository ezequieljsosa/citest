#!/usr/bin/env python3

from bottle import route, run,request

@route('/')
def index():
    name = request.query.name
    age = request.query.age
    if name and age:
        return f'{name} tiene {age} '
    else:
        return "Hola que tal"
if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)