from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

def profile(request):
    """ View to show the user profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This confirms a past order with reference number{order_number}. '
        'An email confirming the order was sent on the day it was placed.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
