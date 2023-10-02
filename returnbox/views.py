from django.shortcuts import render

# Create your views here.

def returnbox(request):
    """ A view to return the returnbox page """

    return render(request, 'returnbox/returnbox.html')