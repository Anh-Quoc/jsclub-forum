from django.shortcuts import render

def custom_error_404(request, *args, **argv):
    return render(request, 'errorPages/error_404.html', {})
