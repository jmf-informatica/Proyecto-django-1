from django.shortcuts import render

def mi_error_404(request, exception):
    return render(request,'core/error_404.html')