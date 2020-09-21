from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cliente, Equipamento, Funcionario, Grupo, Marca, Servico

from django.urls import reverse_lazy
# Create your views here.
class MarcaCreate(CreateView):
    model = Marca
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class GrupoCreate(CreateView):
    model = Grupo
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class EquipamentoCreate(CreateView):
    model = Equipamento
    fields = ['nome_eq','fornecedor','marca','grupo','valor_compra','valor_venda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ServicoCreate(CreateView):
    model = Servico
    fields = ['descricao','tipo_servico','valor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome_cliente','documento','cep','endereco','numero','bairro','cidade','celular','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome_funcionario','cep','endereco','numero','bairro','cidade','celular','email','cargo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

########## UPDATES ########## 
class MarcaUpdate(UpdateView):
    model = Marca
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class GrupoUpdate(UpdateView):
    model = Grupo
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class EquipamentoUpdate(UpdateView):
    model = Equipamento
    fields = ['nome_eq','fornecedor','marca','grupo','valor_compra','valor_venda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ServicoUpdate(UpdateView):
    model = Servico
    fields = ['descricao','tipo_servico','valor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome_cliente','documento','cep','endereco','numero','bairro','cidade','celular','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome_funcionario','cep','endereco','numero','bairro','cidade','celular','email','cargo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

########## DELETE ########## 
class MarcaDelete(DeleteView):
    model = Marca
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class GrupoDelete(DeleteView):
    model = Grupo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class EquipamentoDelete(DeleteView):
    model = Equipamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class ServicoDelete(DeleteView):
    model = Servico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
