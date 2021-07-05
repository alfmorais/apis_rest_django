import requests

# base da aplicação
headers = {'Authorization': 'Token 0fc7ee81e0ca107ef62759bde5101522a86a8dad'}
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

# teste GET
resultado = requests.get(url=url_base_cursos, headers=headers)
print(resultado.json())

# testando se o endpoint está correto
assert resultado.status_code == 200

# testando a quantidade de registro
assert resultado.json()['count'] == 2

# testando se o titulo está correto
assert resultado.json()[
    'results'][0]['titulo'] == 'Python Django - The Practical Guide'
