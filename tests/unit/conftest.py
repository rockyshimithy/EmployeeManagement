#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import factory.django

from manager.models import Employee


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    name = "Joao Lasanha"
    email = "joao@lasanha.com"
    department = "TI"


@pytest.fixture()
def employee():
    return EmployeeFactory()


@pytest.fixture()
def employees(employee):
    employees = [
        employee,
        EmployeeFactory(name='Maria Carbonara', email='maria@carbonara.com', department='Design'),
        EmployeeFactory(name='Leonardo Almondega', email='leonardo@almondega.com', department='TI'),
        EmployeeFactory(name='Ada Bacon', email='ada@bacon.com', department='TI'),
        EmployeeFactory(name='Rafael Jalapeno', email='rafael@jalapeno.com', department='RH'),
        EmployeeFactory(name='Renata Pilsen', email='renata@pilsen.com', department='Design')
        ]

    return employees


