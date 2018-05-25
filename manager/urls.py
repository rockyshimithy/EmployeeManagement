#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name=views.EmployeeList.name),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name=views.EmployeeDetail.name),
]
