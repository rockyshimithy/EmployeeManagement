#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .filters import EmployeeFilter
from .models import Employee
from .serializers import EmployeeSerializer


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


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        import ipdb;  ipdb.set_trace()
        return Response({
            'Employees': reverse(viewname=EmployeeList.name, request=request)
        })


#
# from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# from .models import DayContent
# from .forms import DayContentForm
#
#
# def daybook_list(request):
#     day_contents = DayContent.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'daybook/daybook_list.html', {'day_contents': day_contents})
#
#
# def daycontent_detail(request, pk):
#     day_content = get_object_or_404(DayContent, pk=pk)
#     return render(request, 'daybook/daycontent_detail.html', {'day_content': day_content})
#
#
# def daycontent_new(request):
#     if request.method == "POST":
#         form = DayContentForm(request.POST)
#         if form.is_valid():
#             daycontent = form.save(commit=False)
#             daycontent.author = request.user
#             daycontent.published_date = timezone.now()
#             daycontent.save()
#             return redirect('daycontent_detail', pk=daycontent.pk)
#     else:
#         form = DayContentForm()
#     return render(request, 'daybook/daycontent_edit.html', {'form': form})
