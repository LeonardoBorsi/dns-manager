from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TLD, Domain, SubDomain
from .forms import DomainForm, SubDomainForm, TLDForm
from django.contrib import messages
    
class DomainListView(ListView):
    model = Domain
    template_name = 'domains/domain-list.html'
    context_object_name = 'domains'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Domain.objects.all()
        return Domain.objects.filter(user=self.request.user)

class DomainDetailView(DetailView):
    model = Domain
    template_name = 'domains/domain-detail.html'  # il nome del tuo template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Otteniamo l'oggetto Domain corrente (il dominio di cui stai visualizzando i dettagli)
        domain = get_object_or_404(Domain, pk=self.kwargs['pk'])
        
        # Filtra i subdomini per questo dominio e aggiungili al contesto
        subdomains = SubDomain.objects.filter(domain=domain)
        context['subdomains'] = subdomains
        
        return context

class DomainCreateView(CreateView):
    model = Domain
    form_class = DomainForm
    template_name = 'domains/create-domain.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class DomainUpdateView(UpdateView):
    model = Domain
    form_class = DomainForm
    template_name = 'domains/update-domain.html'

class DomainDeleteView(DeleteView):
    model = Domain
    template_name = 'domains/delete-domain.html'
    success_url = '/domains'

class AcceptDomainView(View):
    def get(self, request, *args, **kwargs):
        domain = get_object_or_404(Domain, pk=kwargs['pk'])
        domain.accepted = True
        domain.save()
        return redirect('domain-detail', pk=kwargs['pk'])

class RejectDomainView(View):
    def get(self, request, *args, **kwargs):
        domain = get_object_or_404(Domain, pk=kwargs['pk'])
        domain.accepted = False
        domain.save()
        return redirect('domain-detail', pk=kwargs['pk'])

class SubDomainDetailView(DetailView):
    model = SubDomain
    template_name = 'domains/subdomain-detail.html'

class SubDomainCreateView(CreateView):
    model = SubDomain
    form_class = SubDomainForm
    template_name = 'domains/create-subdomain.html'

    def form_valid(self, form):
        domain = get_object_or_404(Domain, pk=self.kwargs['pk'])
        form.instance.domain = domain
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('subdomain-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain'] = get_object_or_404(Domain, pk=self.kwargs['pk'])
        return context
    
class SubDomainUpdateView(UpdateView):
    model = SubDomain
    form_class = SubDomainForm
    template_name = 'domains/update-subdomain.html'
    
    def get_success_url(self):
        return reverse('subdomain-detail', kwargs={'pk': self.object.pk})
    
class SubDomainDeleteView(DeleteView):
    model = SubDomain
    template_name = 'domains/delete-subdomain.html'

    def get_success_url(self):
        # Ottieni l'ID del domain a cui apparteneva il subdomain
        domain_id = self.object.domain.id
        # Usa questo ID per costruire l'URL di successo
        return reverse('domain-detail', args=[domain_id])
    
class TLDListView(ListView):
    model = TLD
    template_name = 'domains/tld-list.html'
    context_object_name = 'tlds'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tlds_in_use = set(Domain.objects.values_list('TLD', flat=True).distinct())
        context['tlds_in_use'] = tlds_in_use
        return context

class TLDCreateView(CreateView):
    model = TLD
    form_class = TLDForm
    template_name = 'domains/create-tld.html'
    success_url = '/domains/tld'

class TLDUpdateView(UpdateView):
    model = TLD
    form_class = TLDForm
    template_name = 'domains/update-tld.html'
    success_url = '/domains/tld'

class TLDDeleteView(DeleteView):
    model = TLD
    template_name = 'domains/delete-tld.html'
    success_url = '/domains/tld'