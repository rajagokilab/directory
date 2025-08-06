from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee-edit'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
]
