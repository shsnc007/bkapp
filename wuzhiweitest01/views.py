from django.shortcuts import render

# Create your views here.
def home(request):
    """
    首页
    """
    return render(request, '/wuzhiweitest01/home.html')

