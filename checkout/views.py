from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LZHYMDFAQv2Hr9sMYnBe7sRTp3T2Tf6a454xUi2T8mKaFvMawiF1aVV8JOHn2FpuF2FjGEcQvJTIvY2tW4HxQUC00cbEcJCqn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)