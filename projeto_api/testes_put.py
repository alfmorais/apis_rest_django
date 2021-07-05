import requests

# base da aplicação
headers = {'Authorization': 'Token 0fc7ee81e0ca107ef62759bde5101522a86a8dad'}
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    'titulo': 'Java 2022 COMPLETO: Do Zero ao Profissional + Projetos!',
    'url': 'https://www.udemy.com/course/fundamentos-de-programacao-com-java-2022/'
}

# buscando um curso para teste e verificar se é valido
curso = requests.get(url=f'{url_base_cursos}6/',
                     headers=headers)
print(curso.json())

# alterando e atualizando um curso
resultado = requests.put(url=f'{url_base_cursos}6/',
                         headers=headers,
                         data=curso_atualizado)

# testando um codigo de HTTP
assert resultado.status_code == 200

# testando o titulo
assert resultado.json()['titulo'] == curso_atualizado['titulo']
