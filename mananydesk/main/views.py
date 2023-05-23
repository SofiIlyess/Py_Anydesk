from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .models import Client,ClientsImport
from .forms import ImportForm
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView
import datetime
import openpyxl
import os
from django.contrib import messages

@login_required
def home(request):
    data = {'clients':Client.objects.all}
    return render(request,'main/home.html',data)

class ClientAddView(LoginRequiredMixin,CreateView):
    model = Client
    fields = ('name','anydesk','session','anypwd','winpwd','tel','tel2','note')
    success_url = '/'

    def form_valid(self, form):
        form.instance.createdby = self.request.user
        return super().form_valid(form)


class ClientDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Client
    success_url = '/'

    def test_func(self):
        c = self.get_object()
        if self.request.user == c.createdby:
            return True
        return False


class ClientUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Client
    fields = ('name','anydesk','session','anypwd','winpwd','tel','tel2','note')
    success_url = '/'

    def form_valid(self, form):
        form.instance.updatedby = self.request.user.username
        form.instance.updatedon = datetime.datetime.now()
        return super().form_valid(form)

    def test_func(self):
        c = self.get_object()
        if self.request.user == c.createdby:
            return True
        return False

class ClientDetailView(LoginRequiredMixin,DetailView):
    model = Client

def Import(request):
    if request.method == 'POST':
        impform = ImportForm(request.POST, request.FILES)
        if impform.is_valid():
            impform.instance.owner = request.user
            impform.save()
            messages.success(request,'File uploaded')
            return redirect('home')
        else:
            messages.warning(request,'File not uploaded. Only xls and xlsx files are allowed')
    else:
        impform = ImportForm()
    return render(request,'main/clientsimport_form.html',{'form':impform})

def FilesList(request):
    data = {'data':ClientsImport.objects.filter(owner=request.user)}
    return render(request,'main/list_import.html',data)

class DataImport(LoginRequiredMixin,CreateView):
    model = ClientsImport
    fields = ['file']
    success_url = '/'

    def form_valid(self, form):
        filename, fileext = os.path.splitext(form.instance.file.name)
        print(filename)
        print(fileext)
        # print(form.instance.file.name)
        form.instance.owner = self.request.user
        return super().form_valid(form)