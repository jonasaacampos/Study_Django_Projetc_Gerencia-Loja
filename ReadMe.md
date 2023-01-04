### Configuração do ambiente

- [ ] Instalar dependências 
  - `pip install django whitenoise gunicorn django-bootstrap5 PyMySQL django-stdimage`
  - `pip freeze > requirements.txt`
- [ ] Iniciar projeto
  - `django-admin startproject gerencia_loja .`
- [ ] Iniciar a aplicação
  - `django-admin startapp core`

- [ ] Criar Banco de dados no MySQL Workbench
  - Criar nova conexão > em mySQL Connection, clique em "+". Dê o nome ao seu arquivo depois salve. Insira a senha do usuário solicitado para abrir a conexão.
  - escreva a query `CREATE DATABASE projeto_gerencia;`
  - 

## Planejamento do projeto e requisitos

### Escopo
> o projeto terá 3 páginas
- [ ] index (para carregar dados)
- [ ] contato (para enviar email)
- [ ] formulario (para salvar dados)



## Referências

- [MySQL Community Dowloads](https://dev.mysql.com/downloads/)