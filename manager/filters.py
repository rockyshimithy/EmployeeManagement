import django_filters
from .models import Employee
#from rest_framework import filters


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    email = django_filters.CharFilter(name="email", lookup_expr='icontains')
    department = django_filters.CharFilter(name='department', lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['name', 'email', 'department']
