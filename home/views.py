from django.shortcuts import render
from .models import SanPham
# Create your views here.
def index(request):
    Data = {'sanpham' : SanPham.objects.all().order_by('-ngaythem')}
    return render(request,'pages/home.html',Data)

def chitiet(request, id):
    chitiet = {'chitiet' : SanPham.objects.get(id = id)}
    return render(request, 'pages/chitiet.html', chitiet)
