from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from products.models import product, Variation

from .models import Cart, CartItem



def view(request):

    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
        cart.total = new_total
        cart.save()
        context = {"cart": cart}
    else:
        empty_message = "your cart is empty"
        context = {"empty": True, "empty_message": empty_message}


    template = 'cart/view.html'
    return render(request, template, context)

def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect('/cart')

    cartitem = CartItem.objects.get(id=id)
    cartitem.delete()
    return HttpResponseRedirect('/cart')
        


def add_to_cart(request, slug):

    try:

        the_id = request.session['cart_id']
    except:

        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:

        prd = product.objects.get(slug=slug)
    except product.DoesNotExists:

        pass
    except:

        pass
    product_var = []

    if request.method == "POST":
            qty = request.POST['qty']
            for item in request.POST:
                key = item
                val = request.POST[key]
                try:

                    v = Variation.objects.get(product=prd, category__iexact=key, title__iexact=val)
                    product_var.append(v)
                except:

                    pass

            try:

                the_id = request.session['cart_id']
            except:

                new_cart = Cart()
                new_cart.save()
                request.session['cart_id'] = new_cart.id
                the_id = new_cart.id

            cart = Cart.objects.get(id=the_id)

            try:

                prd = product.objects.get(slug=slug)
            except product.DoesNotExists:

                pass
            except:

                pass

            cart_item = CartItem.objects.create(cart=cart,product=prd)
            if len(product_var) > 0: 
                cart_item.Variations.add(*product_var)
            cart_item.quantity = qty
            cart_item.save()
            request.session['items_total'] = cart.cartitem_set.count()
            print("hello")
            return HttpResponseRedirect('/cart')
    return HttpResponseRedirect('/cart')



