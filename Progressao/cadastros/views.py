from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Cliente, Equipamento, Funcionario, Grupo, Marca, Servico

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.
class MarcaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Marca
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-marca')

class GrupoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Grupo
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-grupo')

class EquipamentoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Equipamento
    fields = ['nome_eq','fornecedor','marca','grupo','valor_compra','valor_venda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-equipamento')

    def form_valid(self, form):

        #Antes do super o meu objeto equipamento ainda não foi criado nem salvo no banco.
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        #Depois do super o objeto está criado.
        return url

class ServicoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Servico
    fields = ['descricao','tipo_servico','valor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servico')

    def form_valid(self, form):

        #Antes do super o meu objeto equipamento ainda não foi criado nem salvo no banco.
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        #Depois do super o objeto está criado.
        return url

class ClienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['nome_cliente','documento','cep','endereco','numero','bairro','cidade','celular','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')

class FuncionarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Funcionario
    fields = ['nome_funcionario','cep','endereco','numero','bairro','cidade','celular','email','cargo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

########## UPDATES ########## 
class MarcaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Marca
    fields = ['nome','descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-marca')

class GrupoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Grupo
    fields = ['descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-grupo')

class EquipamentoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Equipamento
    fields = ['nome_eq','fornecedor','marca','grupo','valor_compra','valor_venda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-equipamento')

class ServicoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Servico
    fields = ['descricao','tipo_servico','valor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servico')

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['nome_cliente','documento','cep','endereco','numero','bairro','cidade','celular','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')

class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Funcionario
    fields = ['nome_funcionario','cep','endereco','numero','bairro','cidade','celular','email','cargo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

########## DELETE ########## 
class MarcaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Marca
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-marca')

class GrupoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Grupo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-grupo')

class EquipamentoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Equipamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-equipamento')

class ServicoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Servico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-servico')

class ClienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cliente')

class FuncionarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionario')

########## LISTA ########## 
class MarcaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Marca
    template_name = 'cadastros/listas/marca.html'

class GrupoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Grupo
    template_name = 'cadastros/listas/grupo.html'

class EquipamentoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Equipamento
    template_name = 'cadastros/listas/equipamento.html'

    def get_queryset(self):
        self.object_list = Equipamento.objects.filter(usuario=self.request.user)
        return self.object_list

class ServicoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Servico
    template_name = 'cadastros/listas/servico.html'

    def get_queryset(self):
        self.object_list = Servico.objects.filter(usuario=self.request.user)
        return self.object_list

class ClienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'cadastros/listas/cliente.html'

class FuncionarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'
