import django_filters
from .models import Employee, Feira


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    email = django_filters.CharFilter(name="email", lookup_expr='icontains')
    department = django_filters.CharFilter(name='department', lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['name', 'email', 'department']

class FeiraFilter(django_filters.FilterSet):
    distrito = django_filters.CharFilter(name='distrito',
                                         lookup_expr='icontains')
    regiao5 = django_filters.CharFilter(name="regiao5",
                                        lookup_expr='icontains')
    nome_feira = django_filters.CharFilter(name='nome_feira',
                                           lookup_expr='iexact')
    bairro = django_filters.CharFilter(name='bairro', lookup_expr='iexact')

    class Meta:
        model = Feira
        fields = ['distrito', 'regiao5', 'nome_feira', 'bairro']
