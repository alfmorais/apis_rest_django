import requests


class TestCursos:
    headers = {'Authorization': 'Token 0fc7ee81e0ca107ef62759bde5101522a86a8dad'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos,
                                headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}10/',
                                headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            'titulo': 'Modelagem de Dados UML (Análise&Projeto Orientado a Objetos)',
            'url': 'https://www.udemy.com/course/uml-diagrama-de-classes/'
        }
        resposta = requests.post(url=self.url_base_cursos,
                                 headers=self.headers,
                                 data=novo)

        assert resposta.status_code == 201
        assert resposta.json() == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            'titulo': 'Novo Modelagem de Dados UML (Análise&Projeto Orientado a Objetos)',
            'url': 'https://www.udemy.com/course/novo-uml-diagrama-de-classes/'
        }
        resposta = requests.put(url=f'{self.url_base_cursos}10/',
                                headers=self.headers,
                                data=atualizado)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}10/',
                                   headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
