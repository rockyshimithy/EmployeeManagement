#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from manager.models import Employee


@pytest.mark.django_db
def test_get_employees(client, employees):
    response = client.get('/employees/')

    assert response.status_code == 200

    for i, employee in enumerate(employees):
        assert response.json()[i]['name'] == employee.name
        assert response.json()[i]['email'] == employee.email
        assert response.json()[i]['department'] == employee.department


@pytest.mark.django_db
def test_get_employees_filtered_by_name(client, employees):
    response = client.get('/employees/?name=Ada')

    employee = Employee.objects.get(name='Ada Bacon')

    assert response.status_code == 200
    assert response.json()[0]['name'] == employee.name
    assert response.json()[0]['email'] == employee.email
    assert response.json()[0]['department'] == employee.department


@pytest.mark.django_db
def test_get_employees_filtered_by_email(client, employees):
    response = client.get('/employees/?email=renata@pilsen.com')

    employee = Employee.objects.get(email='renata@pilsen.com')

    assert response.status_code == 200
    assert response.json()[0]['name'] == employee.name
    assert response.json()[0]['email'] == employee.email
    assert response.json()[0]['department'] == employee.department


@pytest.mark.django_db
def test_get_employees_filtered_by_department(client, employees):
    response = client.get('/employees/?department=TI')

    employees = Employee.objects.filter(department='TI')

    for i, employee in enumerate(employees):
        assert response.json()[i]['name'] == employee.name
        assert response.json()[i]['email'] == employee.email
        assert response.json()[i]['department'] == employee.department


@pytest.mark.django_db
def test_get_employee(client, employees):
    response = client.get('/employee/2/')

    assert response.status_code == 200

    assert 2 == employees[1].id
    assert response.json()['name'] == employees[1].name
    assert response.json()['email'] == employees[1].email
    assert response.json()['department'] == employees[1].department


@pytest.mark.django_db
def test_get_employee_that_does_not_exist(client):
    response = client.get('/employee/999/')

    assert response.status_code == 404
    assert response.json()['detail'] == 'Not found.'


@pytest.mark.django_db
def test_post_employees():
    pass


@pytest.mark.django_db
def test_delete_employees():
    pass
