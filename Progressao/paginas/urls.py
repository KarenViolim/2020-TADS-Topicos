from django.urls import path

# Importa as views que a gente criou 
from .views import PaginaInicial, PaginaSobre, PaginaSobre2, PaginaAjuda

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', PaginaSobre.as_view(), name='sobre'),
    path('sobre2/', PaginaSobre2.as_view(), name='sobre2'),
    path('ajuda/', PaginaAjuda.as_view(), name='ajuda'),
]
