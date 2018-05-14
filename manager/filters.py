#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    email = django_filters.CharFilter(name="email", lookup_expr='icontains')
    department = django_filters.CharFilter(name='department', lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['name', 'email', 'department']
