from django.shortcuts import render

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