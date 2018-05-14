#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    url(r'^employees/$', views.EmployeeList.as_view(), name=views.EmployeeList.name),

    url(r'^employees/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view(), name=views.EmployeeDetail.name),

    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),

    # path('', views.daybook_list, name='daybook_list'),
    # # url(r'^$', views.daybook_list, name='daybook_list'),
    #
    # path('daycontent/<int:pk>/', views.daycontent_detail, name='daycontent_detail'),
    # # url(r'^daycontent/(?P<pk>[0-9]+)/$', views.daycontent_detail, name='daycontent_detail'),
    #
    # path('daycontent/new/', views.daycontent_new, name='daycontent_new'),
    # # url(r'^daycontent/new/$', views.daycontent_new, name='daycontent_new'),
]

