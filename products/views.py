from django.shortcuts import render
from django.http import Http404


# Create your views here.

from .models import product, productImage


def search(request):
	try:
		q = request.GET.get('search')
		print("hello")
		print(q)
	except:
		q = None
	if q:
		products = product.objects.filter(title__icontains=q)
		context = {'query': q, 'products':products}
		template = 'products/results.html'
		print(products)
	else:
		context = {}
		template = 'products/home.html'
	return render(request, template, context)

def home(request):

	products = product.objects.all()
	template = 'products/home.html'
	context = {'products':products}
	return render(request, template, context)

def all(request):

	products = product.objects.all()
	print("inside all")
	context = {'products':products}
	return render(request, 'products/all.html', context)

def single(request, slug):
	
	try:
		single_product = product.objects.get(slug=slug)
		images = productImage.objects.filter(product=single_product)
		context = {'product': single_product, 'images':images}
		template = 'products/single.html'
		return render(request, template, context)
	except:
		raise Http404
	
		
