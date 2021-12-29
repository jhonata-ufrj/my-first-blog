from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),#comando para redirecionar o endereço raíz do projeto à view(que ainda será criada, rs) 'post_list'
    
]
