from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin
from .models import Emp, Dept
from .forms import DeptForm, EmpForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def emp_list(request):
    # Use 'dept' (the name of the ForeignKey field), not 'deptno'
    employees = Emp.objects.select_related('dept').all()
    depts = Dept.objects.all()
    return render(request, 'Employee/index.html', {
        'employees': employees, 
        'depts': depts 
    })

class DeptListView(ListView):
    model = Dept
    context_object_name = 'depts'

class DeptDetailView(DetailView):
    model = Dept

class DeptCreateView(CreateView):
    model = Dept
    form_class = DeptForm
    success_url = reverse_lazy('dept-list')

class DeptupdateView(UpdateView):
    model = Dept
    form_class = DeptForm
    success_url = reverse_lazy('dept-list')

class DeptDeleteView(DeleteView):
    model = Dept
    success_url = reverse_lazy('dept-list')

    