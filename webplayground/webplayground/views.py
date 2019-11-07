from django.shortcuts import render

def mi_error_404(request, exception):
    return render(request,'core/404.html')
