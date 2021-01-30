from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import ExtendedUserCreationForm, OpportunityForm
from main.models import Account, Opportunity


def home(request):
    return render(request, 'main/home.html')


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            messages.success(request, f'Account created for {username} !')
            return redirect('/')
    else:
        form = ExtendedUserCreationForm()

    return render(request, 'main/register.html', {'form': form})


class AccountListView(ListView):
    model = Account
    template_name = 'main/home.html'
    context_object_name = 'accounts'
    paginate_by = 3


class AccountDetailView(DetailView):
    model = Account


class AccountCreateView(LoginRequiredMixin,  SuccessMessageMixin, CreateView):
    model = Account
    fields = ['image', 'name', 'location', 'address']
    success_message = 'account created successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Account
    fields = ['image', 'name', 'location', 'address']
    success_message = 'account updated successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        account = self.get_object()
        if self.request.user == account.user:
            return True
        return False


class AccountDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Account
    success_url = '/'

    def test_func(self):
        account = self.get_object()
        if self.request.user == account.user:
            return True
        return False


class OpportunityListView(ListView):
    model = Opportunity
    context_object_name = 'opportunities'
    paginate_by = 3


class OpportunityDetailView(DetailView):
    model = Opportunity


def create_opportunity(request, pk):
    account = Account.objects.get(id=pk)
    form = OpportunityForm(initial={'account': account})
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Opportunity created successfully!')
            return redirect('/')
    context = {'form': form}
    return render(request, 'main/opportunity_form.html', context)


class OpportunityCreateView(LoginRequiredMixin, CreateView):
    model = Opportunity
    fields = ['account', 'title', 'amount', 'stage']


class OpportunityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Opportunity
    fields = ['account', 'title', 'amount', 'stage']
    success_message = 'opportunity updated successfully'

    def form_valid(self, form):
        form.instance.account.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        opportunity = self.get_object()
        if self.request.user == opportunity.account.user:
            return True
        return False


class OpportunityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Opportunity
    template_name = 'main/opportunity_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        opportunity = self.get_object()
        if self.request.user == opportunity.account.user:
            return True
        return False

