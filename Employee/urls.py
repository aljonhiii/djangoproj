from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_list, name='emp_list'),
    path('dept/', views.DeptListView.as_view(), name='dept-list'),
    path('dept/<int:pk>/', views.DeptDetailView.as_view(), name='dept-detail'),
    path('dept/new/', views.DeptCreateView.as_view(), name='dept-create'),
    path('dept/<int:pk>/update/', views.DeptupdateView.as_view(), name='dept-update'),
    path('dept/<int:pk>/delete/', views.DeptDeleteView.as_view(), name='dept-delete'),
]
