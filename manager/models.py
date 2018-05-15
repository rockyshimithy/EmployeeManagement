#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=200, verbose_name='Name')
    email = models.EmailField(max_length=200, verbose_name='E-mail', unique=True)
    department = models.CharField(max_length=50, verbose_name='Department')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name
