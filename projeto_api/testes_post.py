import requests

# base da aplicação
headers = {'Authorization': 'Token 0fc7ee81e0ca107ef62759bde5101522a86a8dad'}
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    'titulo': 'Java 2021 COMPLETO: Do Zero ao Profissional + Projetos!',
    'url': 'https://www.udemy.com/course/fundamentos-de-programacao-com-java/'

}

resultado = requests.post(url=url_base_cursos,
                          headers=headers,
                          data=novo_curso)

# Testando se o codigo de status HTTP 201
assert resultado.status_code == 201

# Testando se o titulo do curso é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']
