from django.shortcuts import render

def cup_start(request):
    return render(request, 'cup_start.html')

def cup_select(request):
    return render(request, 'cup_select.html')

def cup_ing(request):
    return render(request, 'cup_ing.html')

def cup_result(request):
    return render(request, 'cup_result.html')

def login(request):
    return render(request, 'login.html')

def main(request):
    return render(request, 'main.html')

def signup(request):
    return render(request, 'signup.html')

def agree(request):
    return render(request, 'agree.html')

def product(request):
    return render(request, 'product.html')

def plus(request):
    return render(request, 'plus.html')

def plus_info(request):
    return render(request, 'plus_info.html')

