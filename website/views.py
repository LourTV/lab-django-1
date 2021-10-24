from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def layout_page_view(request):
	return render(request, 'website/layout.html')

def sobre_page_view(request):
	return render(request, 'website/sobre.html')

def inicio_page_view(request):
	return render(request, 'website/inicio.html')

def home_page_view(request):
	return render(request, 'website/home.html')