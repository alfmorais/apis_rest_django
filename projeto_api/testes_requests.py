import requests

# GET Avaliações
avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# Acessando o codigo de status HTTP
print(avaliacoes.status_code)

# Acessando os dados da resposta
print(avaliacoes.json())
print(type(avaliacoes.json()))

# Acessando a quantidade de registros
print(avaliacoes.json()['count'])

# Acessando a proxima pagina de registros
print(avaliacoes.json()['next'])

# Acessando os resultados dessa pagina
print(avaliacoes.json()['results'])
print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
print(avaliacoes.json()['results'][0])

# Acessando o ultimo elemento da lista de resultados
print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a ultima avaliação
print(avaliacoes.json()['results'][-1]['nome'])

# GET AVALIAÇÃO
avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/7/')
print(avaliacao.json())

# GET CURSOS
headers = {'Authorization': 'Token 0fc7ee81e0ca107ef62759bde5101522a86a8dad'}
cursos = requests.get(
    url='http://127.0.0.1:8000/api/v2/cursos/',
    headers=headers)
print(cursos.status_code)
print(cursos.json())
