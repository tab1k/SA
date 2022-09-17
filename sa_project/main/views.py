from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.


def index(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request, 'main/about_us.html')

def favorite(request):
    return render(request, 'main/favorite.html')

def market(request):
    return render(request, 'main/market.html')

def orders(request):
    return render(request, 'main/orders.html')

def sale(request):
    return render(request, 'main/sale.html')

def login(request):
    return render(request, 'main/login.html')

def signin(request):
    return render(request, 'main/signin.html')


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'main/signin.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

