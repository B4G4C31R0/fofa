from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('adicionar_planejamento', adicionar_planejamento, name='adicionar_planejamento'),
    
    path('fatores/<int:id>', fatores, name='fatores'),
    path('objetivo/<int:id>', objetivo, name='objetivo'),
    path('elementos/<int:id>', elementos, name='elementos'),
    path('adicionar_fatores/<int:id>', adicionar_fatores, name='adicionar_fatores'),
    path('adicionar_objetivo/<int:id>', adicionar_objetivo, name='adicionar_objetivo'),
    path('liderElemento/<int:id>/<int:membro>', liderElemento, name='liderElemento'),
    path('comentarioFator/<int:id>', comentarioFator, name='comentarioFator'),

    path('editarMembro/<int:id_plan>/<int:id_memb>', editarMembro, name='editarMembro'),
    path('editarFator/<int:id>', editarFator, name= 'editarFator'),


    path('base',base,name='base'),
    path('teste',teste,name='teste'),
]
