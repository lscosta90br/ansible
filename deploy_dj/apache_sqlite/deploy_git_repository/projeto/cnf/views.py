from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Porta

class PortaListView(ListView):
    model = Porta
    template_name = 'all/porta_list-view.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'portas'
    ordering = ['-data_publicacao']
    paginate_by = 5


class PortaDetailView(DetailView):
    model = Porta
    template_name = 'all/old/porta_detail.html'

class PortaCreateView(LoginRequiredMixin, CreateView):
    model = Porta
    template_name = 'all/porta_form.html'
    success_url = '/cnf/all/'
    fields = ['modelo', 'andar', 'porta_1', 'porta_2', 'observacao', 'autor']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if form.instance.modelo == 'telefone voice unitário':
            form.instance.porta_2 = ''
        form.instance.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PortaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Porta
    template_name = 'all/porta_form.html'
    success_url = '/cnf/all/'
    fields = ['modelo', 'andar', 'porta_1', 'porta_2', 'observacao', 'autor']
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        if form.instance.modelo == 'telefone voice unitário':
            form.instance.porta_2 = ''
        form.instance.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        porta = self.get_object()
        if self.request.user == porta.autor:
            return True
        return True #adicionar False para só usuário que criou fazer update


class PortaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Porta
    template_name = 'all/porta_confirm_delete.html'
    success_url = '/cnf/all/'

    def test_func(self):
        porta = self.get_object()
        if self.request.user == porta.autor:
            return True
        return True #adicionar False para só usuário que criou poder apagar


class PortaGeraDetailView(DetailView):
    model = Porta
    template_name = 'all/porta_gera.html'