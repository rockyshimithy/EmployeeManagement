# EmployeeManagement

## App for CRUD of Employees - using python3.6, Django, Django Rest Framework and SQLite

Antes de começar, é necessário a criação e ativação de uma VirtualEnv com Python 3.6, para isso recomendo pyenv.
Após isso, vá para a pasta raiz desse projeto (EmployeeManagement) e siga as instruções abaixo.

1) Instale os requisitos do projeto

    ```
    $ make requirements
    ```

2) Faça a migração e suba a aplicação (para que possa importar os dados via API REST no próximo passo)

    ```
    $ make migrate_db
    $ make runserver
    ```


# Testando com curl:

(NOTA: Uma alternativa ao curl é a UI Web para interagir com a API via browser, que é habilitada automaticamente pelo django-rest-framework. É possível fazer todas as requisições - GET, POST, PUT, PATCH e DELETE, acessando a seguinte URL: ``` http://127.0.0.1:8000/ ``` . Basta ir navegando pelos links dos recursos.)


- Retorna todas as Employees, também é possível realizar paginação com limit e offset

    ```
    $ curl -iX GET http://127.0.0.1:8000/employees/
    $ curl -X GET http://127.0.0.1:8000/employees/ | python -m json.tool # pretty view
    $ curl -X GET http://127.0.0.1:8000/employees/?limit=10&offset=10
    ```

    ```

    ```

- Cadastra uma nova Employee

    ```
    $ curl -iX POST -H "Content-Type: application/json" -d '{"name":"Joao Roberto", "email": "joao@roberto.com", "department": "TI"}' http://127.0.0.1:8000/employees/
    ```

    ```

    ```

- Deleta uma Employee usando sua Primary Key

    ```
    $ curl -iX DELETE http://127.0.0.1:8000/employee/3/
    ```

    ```

    ```

- Altera os campos de uma employee já cadastrada, exceto a Primary Key

    ```
    $ curl -iX PUT -H "Content-Type: application/json" -d '{"name":"Ada"}' http://127.0.0.1:8000/employee/1/
    ```

    ```

    ```

- Procura por employees usando qualquer um dos seguintes parâmetros (name, email, department)

    ```
    $ curl -X GET http://127.0.0.1:8000/employees/?department=TI | python -m json.tool
    ```

    ```

    ```


























### TODO : REVIEW THIS
- A aplicação suporta os seguintes content types, e não é necessário enviar "Content-Type" no header da requisição:

    ```
    application/json (DEFAULT)
    application/x-www-form-urlencoded
    multipart/form-data
    ```


# Para observar a cobertura dos testes, rode os seguintes comandos

    ```
    $ python EmployeeManagement/manage.py test -v 2 employeemanagement --with-coverage --cover-html
    ```

NOTA: A cobertura do relatório de testes pode ser acessada no arquivo ```EmployeeManagement/employeemanagement/cover/index.html```. Ao clicar em um arquivo do relatório, você pode visualizar a cobertura linha por linha.