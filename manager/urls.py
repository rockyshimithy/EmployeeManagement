#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    #url(r'^employees/$', views.EmployeeList.as_view(), name=views.EmployeeList.name),
    path('employees/', views.EmployeeList.as_view(), name=views.EmployeeList.name),

    #url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view(), name=views.EmployeeDetail.name),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name=views.EmployeeDetail.name),
]

