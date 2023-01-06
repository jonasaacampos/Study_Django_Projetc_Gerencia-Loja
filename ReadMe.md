### Configuração do ambiente

- [ ] Instalar dependências 
  - `pip install django whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage MySQL`
  - `pip freeze > requirements.txt`
- [ ] Iniciar projeto
  - `django-admin startproject gerencia_loja .`
- [ ] Iniciar a aplicação
  - `django-admin startapp core`

- [ ] Criar Banco de dados no MySQL Workbench
  - Criar nova conexão > em mySQL Connection, clique em "+". Dê o nome ao seu arquivo depois salve. Insira a senha do usuário solicitado para abrir a conexão.
  - escreva a query `CREATE DATABASE projeto_gerencia;`

### Iniciar Projeto

- [ ] `python .\manage.py migrate` para criar banco de dados
- [ ] `python manage.py createsuperuser`
- [ ] `python manage.py runserver`

### Ferramentas úteis

Para listar todas as possibilidades dos Forms
```python
#python .\manage.py shell
from django import forms
dir(forms)

for method in dir(forms): 
	print(method)

## para ajuda    
help(forms.CharField)
```

## Planejamento do projeto e requisitos

### Escopo
> o projeto terá 3 páginas
- [ ] index (para carregar dados)
- [ ] contato (para enviar email)
- [ ] formulario (para salvar dados)

**Regras de negócio**

- [ ] Definir rotas administrativas do projeto, inserindo um include e criar um arquivo de rotas na aplicação

## Referências e Ferramentas

- [MySQL Community Dowloads](https://dev.mysql.com/downloads/)
- [Git Ignore Generator](https://mrkandreev.name/snippets/gitignore-generator/#Python,Django,VirtualEnv,PyCharm+all,VisualStudioCode)