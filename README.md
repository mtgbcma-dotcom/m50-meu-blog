# Meu Blog — M50

Projeto de blog desenvolvido para a atividade M50 do curso Full Stack Python da EBAC.

## Implementação

Implementei o modelo Post com título, conteúdo, autor e datas de criação,
atualização e publicação. Incluí a migração inicial e o cadastro no Django Admin.
A página inicial lista os posts publicados; rascunhos e posts com data futura
não são exibidos.

Configurei o pytest com pytest-django e desenvolvi testes para criação e
persistência do Post, representação textual, publicação, ordenação, validação
e relacionamento com o autor. Também incluí testes da página inicial.

## Ambiente

Python 3.10 ou superior. Dependências em requirements.txt.
Projeto independente com Django 5.2.18, pytest 9.1.1 e pytest-django 4.14.0.

## Executar no Windows / PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Abra http://127.0.0.1:8000/ e http://127.0.0.1:8000/admin/.
No admin, cadastre um post com o usuário criado como autor. Para publicar,
preencha a data de publicação ou use a ação “Publicar posts selecionados”.

## Testes

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

A suíte contém 9 testes. Os testes de banco utilizam um banco de testes isolado.
A validação de campos é verificada com full_clean(), pois save() não chama
full_clean() automaticamente.

## Estrutura

- config/: configurações e URLs do projeto.
- blog/models.py: modelo Post.
- blog/migrations/0001_initial.py: migração inicial.
- blog/tests.py: testes automatizados.
- blog/admin.py: administração dos posts.
- blog/views.py e blog/templates/: listagem dos posts.
- pytest.ini: configuração do pytest-django.

## Entrega

Branch de desenvolvimento: models. Pull Request direcionado à main,
mantido aberto para avaliação. Consulte GUIA_VSCODE.md para o procedimento.

## Autor

Bruno Macedo
