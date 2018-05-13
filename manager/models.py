from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=200, verbose_name='Name')
    email = models.CharField(max_length=200, verbose_name='E-mail')
    department = models.CharField(max_length=200, verbose_name='Department')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ["-name"]

    def __str__(self):
        return self.title