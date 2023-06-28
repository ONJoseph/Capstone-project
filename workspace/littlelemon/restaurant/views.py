from django.shortcuts import render

# Create your views here.

def restaurant_view(request):
    return render(request, 'index.html', {})
  
