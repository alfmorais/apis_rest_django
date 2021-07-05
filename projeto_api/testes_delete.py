import requests

# base da aplicação
headers = {'Authorization': 'Token 0fc7ee81e0ca107ef62759bde5101522a86a8dad'}
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

# teste DELETE
resultado = requests.get(url=f'{url_base_cursos}6/',
                         headers=headers)

# testando o codigo HTTP
assert resultado.status_code == 202

# testando se o conteudo = 0
assert len(resultado.text) == 0
