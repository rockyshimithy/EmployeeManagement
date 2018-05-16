#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from manager.models import Employee


@pytest.fixture()
def employee():
    employee = Employee.objects.create(
        name='Joao Lasanha',
        email='joao@lasanha.com',
        department='TI'
    )
    
    return employee


@pytest.fixture()
def employees(employee):
    employees = []

    employees.append(employee)

    employees.append(
        Employee.objects.create(name='Maria Carbonara', email='maria@carbonara.com', department='Design')
    )
    employees.append(
        Employee.objects.create(name='Leonardo Almondega', email='leonardo@almondega.com', department='TI')
    )
    employees.append(
        Employee.objects.create(name='Ada Bacon', email='ada@bacon.com', department='TI')
    )
    employees.append(
        Employee.objects.create(name='Rafael Jalapeno', email='rafael@jalapeno.com', department='RH')
    )
    employees.append(
        Employee.objects.create(name='Renata Pilsen', email='renata@pilsen.com', department='Design')
    )

    return employees
