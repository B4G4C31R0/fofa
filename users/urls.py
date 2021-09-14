from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('registro', registro, name='registro'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('adicionar_membros/<int:id>', adicionar_membros, name='adicionar_membros'),
    path('add_membro',add_membro,name='add_membro'),
    # path('add_membro/<int:id>/<int:usuario>',add_membro,name='add_membro'),
    path('getUsuarios/<int:id>', getUsuarios, name='getUsuarios'),
    path('perfil/<int:id>', perfil, name='perfil'),

    path('logar', logar_usuario, name='logar_usuario'),
    path('logout', logout_view, name='logout_view'),

    path('getConvites/<int:id>', getConvites, name='getConvites'),
    path('convites/<int:id>', convites, name='convites'),
    path('novoConvite', novoConvite, name='novoConvite'),
    # path('novoConvite/<int:convidadoId>/<int:planejamento>', novoConvite, name='novoConvite'),
    path('convRecusado/<int:id>/<int:membro>', convRecusado, name='convRecusado'),
    path('convAceito/<int:id>/<int:idplan>/<int:conv>', convAceito, name='convAceito'),

]
