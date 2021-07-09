from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('adicionar_planejamento', adicionar_planejamento, name='adicionar_planejamento'),
    path('planejamento/<int:id>', planejamento, name='planejamento'),
    path('elementos/<int:id>', elementos, name='elementos'),
    path('adicionar_fatores/<int:id>', adicionar_fatores, name='adicionar_fatores'),
]
