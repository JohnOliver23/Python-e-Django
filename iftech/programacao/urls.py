from django.urls import path
from . import views

urlpatterns = [
    path('', views.atividades, name='atividades'),
    path('<int:atividade_id>/', views.atividade, name="atividade"),
    path('edit/<int:atividade_id>/', views.atividade_edit, name="atividade_edit"),
]