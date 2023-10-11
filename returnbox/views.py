from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from profiles.models import UserProfile
from .models import BoxReturn
import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Feedback
from .forms import FeedbackForm
from .forms import NewsletterSubscriptionForm


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

@login_required
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


@login_required
def remove_box_return(request, box_return_id):
    # Fetch the box return object by ID
    box_return = get_object_or_404(BoxReturn, id=box_return_id)

    if box_return.status == 'pending':
        user_profile = box_return.user
        quantity = box_return.number_of_boxes_returned
        
        # Update user's box balance before removing the box return request
        user_profile.box_balance += quantity
        user_profile.save()
        
        # Add your logic to handle the remove action (e.g., deleting the box return)
        box_return.delete()

        messages.success(request, f'Successfully removed box return request.')

    return redirect('returnbox')  # Redirect back to the returnbox page


@login_required
def feedback(request):
    form = FeedbackForm()

    # Query the Feedback model to get user's feedback submissions
    user_feedback = Feedback.objects.filter(user=request.user)

    return render(request, 'returnbox/feedback.html', {'form': form, 'user_feedback': user_feedback})


@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            user = request.user
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            feedback = Feedback(user=user, subject=subject, message=message)
            feedback.save()

            messages.success(request, 'Thank you for your feedback!')

            return redirect('returnbox')  # Redirect to a relevant page

    else:
        form = FeedbackForm()

    return render(request, 'returnbox/feedback.html', {'form': form})


def subscribe_newsletter(request):
    form = NewsletterSubscriptionForm()
    return render(request, 'returnbox/subscribe.html', {'form': form})
