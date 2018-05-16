# EmployeeManagement

## App para CRUD de Funcionários - usando python3.6, Django, Django Rest Framework e SQLite

Antes de começar, é necessário a criação e ativação de uma VirtualEnv com Python 3.6, para isso recomendo pyenv.
Após isso, vá para a pasta raiz desse projeto (EmployeeManagement) e siga as instruções abaixo.

1) Instale os requisitos do projeto

    ```shell
    $ make requirements
    ```

2) Faça a migração e suba a aplicação

    ```shell
    $ make migrate_db
    $ make runserver
    ```


# Testando com curl:

(NOTA: Uma alternativa ao curl é a UI Web para interagir com a API via browser, que é habilitada automaticamente pelo django-rest-framework. É possível fazer todas as requisições - GET, POST, PUT, PATCH e DELETE, acessando a seguinte URL: ``` http://127.0.0.1:8000/employees/ ``` . Basta ir navegando pelos links dos recursos.)


- Retorna todas os Funcionários

    ```shell
    $ curl -iX GET http://127.0.0.1:8000/employees/
    $ curl -X GET http://127.0.0.1:8000/employees/ | python -m json.tool # pretty view
    ```

    ```
    [
        {
            "department": "TI",
            "email": "joao@roberto.com",
            "name": "Joao Roberto"
        },
        {
            "department": "TI",
            "email": "joao@roberto2.com",
            "name": "Joao Roberto"
        },
        {
            "department": "TI",
            "email": "joao@roberto3.com",
            "name": "Joao Roberto"
        },
        {
            "department": "TI",
            "email": "joao@roberto4.com",
            "name": "Joao Roberto"
        },
        {
            "department": "TI",
            "email": "joao@roberto5.com",
            "name": "Joao Roberto"
        }
    ]

    ```
    
 - Retorna um Funcionário especifico, usando sua primary key

    ```shell
    $ curl -iX GET http://127.0.0.1:8000/employee/1/
    $ curl -X GET http://127.0.0.1:8000/employee/1/ | python -m json.tool # pretty view
    ```

    ```
    HTTP/1.1 200 OK
    Date: Wed, 16 May 2018 01:59:49 GMT
    Server: WSGIServer/0.2 CPython/3.6.0
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: SAMEORIGIN
    Content-Length: 68
    
    {"name":"Joao Roberto","email":"joao@roberto.com","department":"TI"}

    ```

- Cadastra um novo Funcionário

    ```shell
    $ curl -iX POST -H "Content-Type: application/json" -d '{"name":"Joao Roberto", "email": "joao@roberto.com", "department": "TI"}' http://127.0.0.1:8000/employees/
    ```

    ```
    HTTP/1.1 201 Created
    Date: Wed, 16 May 2018 01:52:57 GMT
    Server: WSGIServer/0.2 CPython/3.6.0
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: SAMEORIGIN
    Content-Length: 68
    
    {"name":"Joao Roberto","email":"joao@roberto.com","department":"TI"}
    ```

- Deleta um Funcionário usando sua Primary Key

    ```shell
    $ curl -iX DELETE http://127.0.0.1:8000/employee/3/
    ```

    ```
    HTTP/1.1 204 No Content
    Date: Wed, 16 May 2018 01:57:29 GMT
    Server: WSGIServer/0.2 CPython/3.6.0
    Vary: Accept, Cookie
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: SAMEORIGIN
    Content-Length: 0
    ```

- Altera os campos de um Funcionário já cadastrado usando PATCH, exceto a Primary Key

    ```shell
    $ curl -iX PATCH -H "Content-Type: application/json" -d '{"name":"Ada"}' http://127.0.0.1:8000/employee/1/
    ```

    ```
    HTTP/1.1 200 OK
    Date: Wed, 16 May 2018 02:01:30 GMT
    Server: WSGIServer/0.2 CPython/3.6.0
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: SAMEORIGIN
    Content-Length: 59
    
    {"name":"Ada","email":"joao@roberto.com","department":"TI"}
    ```
    
- Altera os campos de um Funcionário já cadastrado usando PUT, exceto a Primary Key

    ```shell
    $ curl -iX PUT -H "Content-Type: application/json" -d '{"name":"Ada Lovelace","email":"ada@lovelace.com","department":"CTO"}' http://127.0.0.1:8000/employee/1/
    ```

    ```
    HTTP/1.1 200 OK
    Date: Wed, 16 May 2018 02:07:48 GMT
    Server: WSGIServer/0.2 CPython/3.6.0
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: SAMEORIGIN
    Content-Length: 69
    
    {"name":"Ada Lovelace","email":"ada@lovelace.com","department":"CTO"
    ```

- Procura por Funcionários usando qualquer um dos seguintes parâmetros (name, email, department)

    ```shell
    $ curl -X GET http://127.0.0.1:8000/employees/?name=Roberto | python -m json.tool
    ```

    ```
    [
        {
            "department": "TI",
            "email": "joao@roberto2.com",
            "name": "Joao Roberto"
        },
        {
            "department": "TI",
            "email": "joao@roberto4.com",
            "name": "Joao Roberto"
        },
        {
            "department": "TI",
            "email": "joao@roberto5.com",
            "name": "Joao Roberto"
        }
    ]
    ```

# Painel Django Admin 

Para poder acessar o painel de django admin é necessário criar um "superuser", execute o comando a seguir para gerar um:

```shell
$ make superuser
```

Acesse a interface através da url http://127.0.0.1:8000/admin 

# Para observar a cobertura dos testes, rode os seguintes comandos

```shell
$ make unit
```
