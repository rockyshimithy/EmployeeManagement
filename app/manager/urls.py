from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name=views.EmployeeList.name),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name=views.EmployeeDetail.name),
    
    path('feiras/', views.FeiraList.as_view(), name=views.FeiraList.name),
    path('feiras/<int:pk>/', views.FeiraDetail.as_view(), name=views.FeiraDetail.name),

    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
