from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Cliente, Equipamento, Funcionario, Grupo, Marca, Servico

from django.urls import reverse_lazy
# Create your views here.
class MarcaCreate(CreateView):
    model = Marca
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-marca')

class GrupoCreate(CreateView):
    model = Grupo
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-grupo')

class EquipamentoCreate(CreateView):
    model = Equipamento
    fields = ['nome_eq','fornecedor','marca','grupo','valor_compra','valor_venda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-equipamento')

class ServicoCreate(CreateView):
    model = Servico
    fields = ['descricao','tipo_servico','valor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servico')

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome_cliente','documento','cep','endereco','numero','bairro','cidade','celular','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome_funcionario','cep','endereco','numero','bairro','cidade','celular','email','cargo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

########## UPDATES ########## 
class MarcaUpdate(UpdateView):
    model = Marca
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-marca')

class GrupoUpdate(UpdateView):
    model = Grupo
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-grupo')

class EquipamentoUpdate(UpdateView):
    model = Equipamento
    fields = ['nome_eq','fornecedor','marca','grupo','valor_compra','valor_venda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-equipamento')

class ServicoUpdate(UpdateView):
    model = Servico
    fields = ['descricao','tipo_servico','valor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servico')

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome_cliente','documento','cep','endereco','numero','bairro','cidade','celular','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome_funcionario','cep','endereco','numero','bairro','cidade','celular','email','cargo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

########## DELETE ########## 
class MarcaDelete(DeleteView):
    model = Marca
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-marca')

class GrupoDelete(DeleteView):
    model = Grupo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-grupo')

class EquipamentoDelete(DeleteView):
    model = Equipamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-equipamento')

class ServicoDelete(DeleteView):
    model = Servico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-servico')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cliente')

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')

########## LISTA ########## 
class MarcaList(ListView):
    model = Marca
    template_name = 'cadastros/listas/marca.html'

class GrupoList(ListView):
    model = Grupo
    template_name = 'cadastros/listas/grupo.html'

class EquipamentoList(ListView):
    model = Equipamento
    template_name = 'cadastros/listas/equipamento.html'

class ServicoList(ListView):
    model = Servico
    template_name = 'cadastros/listas/servico.html'

class ClienteList(ListView):
    model = Cliente
    template_name = 'cadastros/listas/cliente.html'

class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'
