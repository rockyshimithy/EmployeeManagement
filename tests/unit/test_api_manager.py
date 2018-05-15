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
def test_get_employee(client, employees):
    response = client.get('/employee/2/')

    assert response.status_code == 200

    assert 2 == employees[1].id
    assert response.json()['name'] == employees[1].name
    assert response.json()['email'] == employees[1].email
    assert response.json()['department'] == employees[1].department


@pytest.mark.django_db
def test_post_employees():
    pass


@pytest.mark.django_db
def test_delete_employees():
    pass