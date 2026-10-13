# M50 — Procedimento completo no VS Code

## Escopo e orientação da atividade

O enunciado da imagem pede branch `models`, modelos com arquivo de migração,
Pull Request e professores da EBAC como revisores. Os comentários acrescentam
um teste automatizado de Post com pytest. Este projeto inclui ambos.

A imagem não informa os campos dos modelos e não foram disponibilizadas as aulas.
Esta é uma implementação funcional de Meu Blog; compare os nomes e campos com
os exemplos do professor antes da entrega. Não foi possível acessar o repositório
Albert5a/mysite durante a preparação. O código foi criado independentemente.

Use um projeto e repositório novos para a M50. Isso permite manter o PR da M49
aberto sem precisar mesclá-lo. Caso o tutor exija continuar no mesmo repositório,
confirme a base do próximo PR com ele.

## 1. Abrir os arquivos

Extraia o ZIP, por exemplo em:
C:\Users\INSPIRON\Desktop\EBAC\EBACc\M50

No VS Code, use Arquivo > Abrir Pasta e selecione a pasta m50-meu-blog que
contém manage.py, README.md e requirements.txt. Use Terminal > Novo Terminal
(PowerShell). O ZIP não contém .venv, .git nem banco local.

## 2. Criar ambiente e instalar

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Não é necessário ativar o ambiente. Não execute startproject ou startapp:
os arquivos do projeto já estão prontos no ZIP.

## 3. Aplicar migrações e verificar

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py makemigrations --check --dry-run
```

A migração blog/migrations/0001_initial.py já está incluída.
O último comando deve informar No changes detected.

## 4. Executar os testes

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Esperado: 9 passed. Se ocorrer erro, corrija antes do envio.
O teste central é test_post_is_saved_with_its_attributes, em blog/tests.py.

## 5. Testar o blog no navegador

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Cadastre usuário e senha. Ao digitar a senha, os caracteres não aparecem no terminal.
Abra http://127.0.0.1:8000/admin/, entre, acesse Posts e adicione título,
conteúdo e autor. Salve, selecione o post e use a ação Publicar posts selecionados.
Abra http://127.0.0.1:8000/ para ver o texto. Pare o servidor com Ctrl+C.
Um print do blog e do resultado dos testes pode complementar o PR, mas não
substitui os arquivos de teste e a migração.

## 6. Criar main e models no terminal

Execute somente na pasta nova da M50:

```powershell
git init
git branch -M main
git add README.md .gitignore
git commit -m "Inicia repositório Meu Blog M50"
git switch -c models
git add .
git status
```

O primeiro commit inclui só README e .gitignore. Assim, os modelos, a migração
e os testes ficam na models e aparecem na comparação do PR.
Confira que .venv, db.sqlite3, __pycache__ e .pytest_cache não estão preparados
para commit. Os diretórios migrations e seus arquivos .py devem estar incluídos.

```powershell
git commit -m "Implementa modelo Post, migração e testes com pytest"
```

Se faltar identidade do Git, configure seu nome e seu e-mail do GitHub:

```powershell
git config user.name "Bruno Macedo"
git config user.email "SEU_EMAIL_DO_GITHUB"
```

Depois repita o commit que apresentou o erro.

## 7. Criar repositório no site do GitHub

Acesse GitHub > + > New repository.
Nome: m50-meu-blog. Visibilidade: Public.
Não adicione README, gitignore ou licença no site: o repositório local já possui
um commit inicial. Clique em Create repository.

## 8. Conectar e enviar pelo VS Code

Para a conta mtgbcma-dotcom, depois de criar o repositório com esse nome:

```powershell
git remote add origin https://github.com/mtgbcma-dotcom/m50-meu-blog.git
git push -u origin main
git push -u origin models
```

Se origin já existir, confira git remote -v antes de alterar qualquer endereço.
Não use push --force. Conclua a autenticação quando solicitada.

## 9. Abrir PR

```powershell
Start-Process "https://github.com/mtgbcma-dotcom/m50-meu-blog/compare/main...models?expand=1"
```

Confira base: main e compare: models. Clique em Create pull request.
Título sugerido: M50 — Modelo Post, migração e testes automatizados.

Descrição (depois de executar os testes no seu notebook):

Implementei o projeto Meu Blog com o modelo Post, incluindo título, conteúdo,
autor e datas de criação, atualização e publicação. Adicionei a migração inicial,
o cadastro no Django Admin e uma página para listar os posts publicados.

Configurei pytest e pytest-django e incluí testes para criação e persistência,
representação textual, publicação, ordenação, validação e relacionamento com o
autor, além de testes da página inicial.

Validação: python manage.py check, verificação de migrações e python -m pytest -v.
Resultado dos testes: 9 passed.

Este PR compara models com main e permanecerá aberto para avaliação.

## 10. Revisores e entrega

A imagem pede os professores da EBAC como revisores. Use apenas os perfis oficiais
indicados pelo curso; nenhum nome de usuário foi informado no material recebido.
Na lateral do PR, em Reviewers, selecione os perfis quando estiverem disponíveis.
Se não aparecerem, peça ao tutor o usuário e a orientação de acesso ao repositório.

Não clique em Merge pull request. Copie o link da página do PR, com /pull/NUMERO,
e envie no campo da atividade M50 da EBAC. Confira que Files changed inclui
blog/models.py, blog/migrations/0001_initial.py, blog/tests.py, pytest.ini
e requirements.txt.

## Verificação realizada na preparação do pacote

Python 3.12.14, Django 5.2.18, pytest 9.1.1, pytest-django 4.14.0.
9 testes passaram; check sem problemas; nenhuma migração pendente.
Repita os comandos no seu notebook para confirmar seu ambiente.

Referências: https://docs.djangoproject.com/en/5.2/topics/db/models/
e https://pytest-django.readthedocs.io/en/latest/
