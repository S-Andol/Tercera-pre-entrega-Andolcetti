from django.urls import path
# from django_clase_18.views import mi_vista, mostrar_fecha
# otra forma de pedir eso:
from inicio import views

# app_name = 'inicio'


urlpatterns = [ 
    
    path ('', views.mi_vista, name = 'inicio'),
    
    path('crear-superheroe/', views.crear_superheroe, name = 'crear_superheroe'),
    path('superheroe/', views.lista_superheroe, name = 'listar_superheroe'),

    
]