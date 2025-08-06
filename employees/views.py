from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Employee

# Filtered list view
class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        queryset = super().get_queryset()
        department = self.request.GET.get('department')
        if department:
            queryset = queryset.filter(department=department)
        return queryset

# Detail view with breadcrumbs
class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = f"Home > {self.object.department} > {self.object.name}"
        return context

# HR-only mixin
class HRPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff  # or add a custom group/role

# CRUD views for HR
class EmployeeCreateView(LoginRequiredMixin, HRPermissionMixin, CreateView):
    model = Employee
    fields = ['name', 'department', 'email', 'phone', 'position']
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(LoginRequiredMixin, HRPermissionMixin, UpdateView):
    model = Employee
    fields = ['name', 'department', 'email', 'phone', 'position']
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(LoginRequiredMixin, HRPermissionMixin, DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')
