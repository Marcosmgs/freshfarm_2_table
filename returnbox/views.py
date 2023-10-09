from django.shortcuts import render, redirect
from django.contrib import messages
from profiles.models import UserProfile
from .models import BoxReturn
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def returnbox(request):
    """ A view to return the returnbox page and display box_balance """
    user_profile = UserProfile.objects.get(user=request.user)

    box_returns = BoxReturn.objects.filter(user=user_profile)
    
    context = {
        'user_profile': user_profile,
        'box_returns': box_returns,
    }

    return render(request, 'returnbox/returnbox.html', context)


def box_return_request(request):
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
    
        if quantity <= 0:
            messages.error(request, 'Invalid quantity. Please enter a positive number of boxes.')
        elif request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            
            if user_profile.box_balance < quantity:
                messages.error(request, 'Insufficient box balance to request this quantity of boxes.')
            else:
                # Handle the box return request logic
                # Deduct the requested quantity from user's box balance
                user_profile.box_balance -= quantity
                user_profile.save()

                box_return = BoxReturn(
                    user=user_profile,
                    number_of_boxes_returned=quantity,
                    status='pending',  # Set the status to 'pending'
                )
                box_return.save()

                print(f'BOXES TO BE RETURNED: {box_return.number_of_boxes_returned}')
                
                messages.success(request, f'Successfully requested {quantity} boxes for return.')
        else:
            # Handle the user is not authenticated
            messages.error(request, 'You need to be logged in to request box return.')

        request.session['box_return_request'] = {
            'quantity': quantity,
            'request_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'pending',
        }

    return redirect('returnbox')  # Redirect back to the returnbox page