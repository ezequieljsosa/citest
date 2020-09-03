import server

def test_webapp_index():
    assert server.index() == 'Hola que tal'
