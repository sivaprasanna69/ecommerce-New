import time

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.urls import reverse

# Create your views here.

from cart.models import Cart
from .models import Order
from .utils import id_generator



def orders(request):
	order = Order.objects.filter(user=request.user).values()
	context = {'order': order}
	template = "orders/user.html"
	return render(request, template, context)


@login_required
def checkout(request):

	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
		print(cart)
	except:
		the_id = None
		return HttpResponseRedirect(reverse("cart:view"))

	try:
		new_order = Order.objects.get(cart=cart)
	except Order.DoesNotExist:
		new_order = Order(cart=cart)
		new_order.user = request.user
		new_order.order_id = str(time.time())
		new_order.save()
	except:
		return HttpResponseRedirect(reverse("cart:view"))


	if new_order.status == "Finished":
		cart.delete()
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse("cart:view"))
		
	context = {}
	template ="products/home.html"
	return render(request, template, context)
