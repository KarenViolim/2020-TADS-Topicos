from django.urls import path

# Importa as views que a gente criou 
from .views import ClienteCreate, EquipamentoCreate, FuncionarioCreate, GrupoCreate, MarcaCreate, ServicoCreate

from .views import ClienteUpdate, EquipamentoUpdate, FuncionarioUpdate, GrupoUpdate, MarcaUpdate, ServicoUpdate

from .views import ClienteDelete, EquipamentoDelete, FuncionarioDelete, GrupoDelete, MarcaDelete, ServicoDelete

from .views import ClienteList, EquipamentoList, FuncionarioList, GrupoList, MarcaList, ServicoList
# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    path('cadastrar/cliente/', ClienteCreate.as_view(), name='cadastrar-cliente'),
    path('cadastrar/equipamento/', EquipamentoCreate.as_view(), name='cadastrar-equipamento'),
    path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name='cadastrar-funcionario'),
    path('cadastrar/grupo/', GrupoCreate.as_view(), name='cadastrar-grupo'),
    path('cadastrar/marca/', MarcaCreate.as_view(), name='cadastrar-marca'),
    path('cadastrar/servico/', ServicoCreate.as_view(), name='cadastrar-servico'),

    path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar-cliente'),
    path('editar/equipamento/<int:pk>/', EquipamentoUpdate.as_view(), name='editar-equipamento'),
    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name='editar-funcionario'),
    path('editar/grupo/<int:pk>/', GrupoUpdate.as_view(), name='editar-grupo'),
    path('editar/marca/<int:pk>/', MarcaUpdate.as_view(), name='editar-marca'),
    path('editar/servico/<int:pk>/', ServicoUpdate.as_view(), name='editar-servico'),

    path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name='excluir-cliente'),
    path('excluir/equipamento/<int:pk>/', EquipamentoDelete.as_view(), name='excluir-equipamento'),
    path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name='excluir-funcionario'),
    path('excluir/grupo/<int:pk>/', GrupoDelete.as_view(), name='excluir-grupo'),
    path('excluir/marca/<int:pk>/', MarcaDelete.as_view(), name='excluir-marca'),
    path('excluir/servico/<int:pk>/', ServicoDelete.as_view(), name='excluir-servico'),

    path('listar/cliente/', ClienteList.as_view(), name='listar-cliente'),
    path('listar/equipamento/', EquipamentoList.as_view(), name='listar-equipamento'),
    path('listar/funcionario/', FuncionarioList.as_view(), name='listar-funcionario'),
    path('listar/grupo/', GrupoList.as_view(), name='listar-grupo'),
    path('listar/marca/', MarcaList.as_view(), name='listar-marca'),
    path('listar/servico/', ServicoList.as_view(), name='listar-servico'),
]