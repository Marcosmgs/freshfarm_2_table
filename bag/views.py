from django.shortcuts import render

def view_bag(request):
    """ View to render the bag content page """
    
    return render(request, 'bag/bag.html')