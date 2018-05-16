#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytest

from manager.models import Employee


@pytest.mark.django_db
def test_success_get_employees(client, employees):
    response = client.get('/employees/')

    assert response.status_code == 200

    for i, employee in enumerate(employees):
        assert response.json()[i]['name'] == employee.name
        assert response.json()[i]['email'] == employee.email
        assert response.json()[i]['department'] == employee.department


@pytest.mark.django_db
def test_success_get_employees_filtered_by_name(client, employees):
    response = client.get('/employees/?name=Ada')

    employee = Employee.objects.get(name='Ada Bacon')

    assert response.status_code == 200
    assert response.json()[0]['name'] == employee.name
    assert response.json()[0]['email'] == employee.email
    assert response.json()[0]['department'] == employee.department


@pytest.mark.django_db
def test_success_get_employees_filtered_by_email(client, employees):
    response = client.get('/employees/?email=renata@pilsen.com')

    employee = Employee.objects.get(email='renata@pilsen.com')

    assert response.status_code == 200
    assert response.json()[0]['name'] == employee.name
    assert response.json()[0]['email'] == employee.email
    assert response.json()[0]['department'] == employee.department


@pytest.mark.django_db
def test_success_get_employees_filtered_by_department(client, employees):
    response = client.get('/employees/?department=TI')

    employees = Employee.objects.filter(department='TI')

    for i, employee in enumerate(employees):
        assert response.json()[i]['name'] == employee.name
        assert response.json()[i]['email'] == employee.email
        assert response.json()[i]['department'] == employee.department


@pytest.mark.django_db
def test_success_post_employee(client):
    data = {'name': 'Max Skywalker', 'email': 'max@skywalker.com', 'department': 'TI'}

    response = client.post('/employees/', data=data)

    employee = Employee.objects.get(name='Max Skywalker')

    assert response.status_code == 201
    assert response.json()['name'] == employee.name
    assert response.json()['email'] == employee.email
    assert response.json()['department'] == employee.department


@pytest.mark.django_db
def test_failed_post_employee_with_empty_name(client):
    data = {'name': '', 'email': 'max@skywalker.com', 'department': 'TI'}

    response = client.post('/employees/', data=data)

    assert response.status_code == 400
    assert response.json()['name'][0] == 'This field may not be blank.'


@pytest.mark.django_db
def test_failed_post_employee_with_empty_email(client):
    data = {'name': 'Max Skywalker', 'email': '', 'department': 'TI'}

    response = client.post('/employees/', data=data)

    assert response.status_code == 400
    assert response.json()['email'][0] == 'This field may not be blank.'


@pytest.mark.django_db
def test_failed_post_employee_with_wrong_format_on_email(client):
    data = {'name': 'Max Skywalker', 'email': 'tchurur.com', 'department': 'TI'}

    response = client.post('/employees/', data=data)

    assert response.status_code == 400
    assert response.json()['email'][0] == 'Enter a valid email address.'


@pytest.mark.django_db
def test_failed_post_employee_with_empty_department(client):
    data = {'name': 'Max Skywalker', 'email': 'max@skywalker.com', 'department': ''}

    response = client.post('/employees/', data=data)

    assert response.status_code == 400
    assert response.json()['department'][0] == 'This field may not be blank.'


@pytest.mark.django_db
def test_failed_post_employee_with_email_that_already_exists(client, employee):
    data = {'name': 'Joao Bolo de Cenoura', 'email': 'joao@lasanha.com', 'department': 'TI'}

    response = client.post('/employees/', data=data)

    assert response.status_code == 400
    assert response.json()['email'][0] == 'Employee with this E-mail already exists.'


@pytest.mark.django_db
def test_success_get_employee(client, employees):
    response = client.get('/employee/2/')

    assert response.status_code == 200

    assert 2 == employees[1].id
    assert response.json()['name'] == employees[1].name
    assert response.json()['email'] == employees[1].email
    assert response.json()['department'] == employees[1].department


@pytest.mark.django_db
def test_failed_get_employee_that_does_not_exist(client):
    response = client.get('/employee/999/')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Not found.'


@pytest.mark.django_db
def test_success_delete_employee(client, employees):
    response = client.delete('/employee/1/')

    employee = Employee.objects.filter(name='Joao Lasanha')

    assert response.status_code == 204
    assert len(employee) == 0


@pytest.mark.django_db
def test_failed_delete_employee_not_found(client):
    response = client.delete('/employee/1/')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Not found.'


@pytest.mark.django_db
def test_success_edit_employee_with_put(client, employees):
    data = {'name': 'Joao Bolo de Cenoura', 'email': 'joao@bolodecenoura.com', 'department': 'IOT'}

    response = client.put('/employee/1/', data=json.dumps(data), content_type='application/json')

    employee = Employee.objects.filter(name='Joao Bolo de Cenoura')

    assert response.status_code == 200
    assert response.json()['name'] == employee[0].name
    assert response.json()['email'] == employee[0].email
    assert response.json()['department'] == employee[0].department


@pytest.mark.django_db
def test_failed_edit_employee_with_put_and_without_some_fields(client, employees):
    data = {'name': 'Joao Bolo de Cenoura'}

    response = client.put('/employee/1/', data=json.dumps(data), content_type='application/json')

    employee = Employee.objects.filter(name='Joao Bolo de Cenoura')

    assert response.status_code == 400
    assert response.json()['email'][0] == 'This field is required.'
    assert response.json()['department'][0] == 'This field is required.'


@pytest.mark.django_db
def test_success_edit_employee_with_patch(client, employees):
    data = {'name': 'Joao Bolo de Cenoura'}

    response = client.patch('/employee/1/', data=json.dumps(data), content_type='application/json')

    employee = Employee.objects.filter(name='Joao Bolo de Cenoura')

    assert response.status_code == 200
    assert response.json()['name'] == employee[0].name
    assert response.json()['email'] == employee[0].email
    assert response.json()['department'] == employee[0].department
