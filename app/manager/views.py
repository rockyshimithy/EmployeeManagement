from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


from .filters import EmployeeFilter, FeiraFilter
from .models import Employee, Feira
from .serializers import EmployeeSerializer, FeiraSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EmployeeFilter
    name = 'employee-list'


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-detail'


class FeiraList(generics.ListCreateAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = FeiraFilter
    name = 'feira-list'


class FeiraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer
    name = 'feira-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'feiras': reverse(FeiraList.name, request=request)
        })
