from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.views import generic, View
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

def all_products(request):
    """ View to display all the products and sorting search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    for product in products:
        product.favorited = False
        if product.is_favorited.filter(id=request.user.id).exists():
            product.favorited = True

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            for product in products:
                product.favorited = False
                if product.is_favorited.filter(id=request.user.id).exists():
                    product.favorited = True            

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            for product in products:
                product.favorited = False
                if product.is_favorited.filter(id=request.user.id).exists():
                    product.favorited = True

            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            for product in products:
                product.favorited = False
                if product.is_favorited.filter(id=request.user.id).exists():
                    product.favorited = True            


    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    product.favorited = False
    if product.is_favorited.filter(id=request.user.id).exists():
        product.favorited = True

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if product.is_favorited.filter(id=request.user.id).exists():
        product.is_favorited.remove(request.user)
        messages.success(request, f'You removed {product.name} from your favorite')
    else:
        product.is_favorited.add(request.user)
        messages.success(request, f'You added {product.name} to your favorite')

    return redirect(request.META['HTTP_REFERER'])

def favorite_products(request):
    """" 
    retrieves a list of favorite products 
    for a specific user and prepares the data 
    to be displayed in a template. 
    """
    user = request.user
    favorite_products = Product.objects.filter(is_favorited=user)
    for product in favorite_products:
        product.favorited = False
        if product.is_favorited.filter(id=request.user.id).exists():
            product.favorited = True            

    
    context = {
        'favorite_products': favorite_products,
    }
    
    return render(request, 'products/favorite_products.html', context)

def add_product(request):
    """ Add products to the shop """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Unable to add product. Please make sure the form is filled out correctly.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    """ Update the shop products """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Unable to update product. Please make sure the form is filled out correctly.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))