from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def error(request):
    return render(request , 'error.html')

def error_404(request,exception):
    return render(request , 'error404.html')

def error_403(request,exception):
    return render(request , 'error403.html')
