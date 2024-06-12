from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from .models import Product, Category, Rating
from .forms import ProductForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def all_products(request):
    """ A view to show all products """

    # Fetch all products and annotate each product with its average rating
    products = Product.objects.annotate(average_rating=Avg('rating__rating'))

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                # Annotate with lowercase name for case-insensitive sorting
                products = products.annotate(lower_name=Lower('name'))
                sortkey = 'lower_name'
            elif sortkey == 'category':
                # Annotate with lowercase category name for case-insensitive sorting
                products = products.annotate(lower_category_name=Lower('category__name'))
                sortkey = 'lower_category_name'
            elif sortkey == 'rating':
                sortkey = 'average_rating'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # Sort products based on the selected sort key
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # Filter products by selected categories
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']    
            # Filter products by search query
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(brand__icontains=query)
            products = products.filter(queries)
    
    # Generate the current sorting information for display in the template
    current_sorting = f'{sort}_{direction}'

    # Products with status == 0
    status_zero_products = products.filter(status=0)

    # Count the number of products with status == 0
    status_zero_count = status_zero_products.count()

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'status_zero_products': status_zero_products,
        'status_zero_count': status_zero_count,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(user=request.user, product=product).exists()
    else:
        user_rating = False  
    # Calculate average rating
    average_rating = Rating.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']

    context = {
        'product': product,
        'user_rating': user_rating,
        'average_rating': average_rating,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('products')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('products')
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owner can do that.')
        return redirect('products')
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')

    return redirect(reverse('products'))


@login_required
def rate_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user
    
    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))    
        # Create a new rating
        new_rating = Rating(user=user, product=product, rating=rating_value)
        new_rating.save()
        messages.success(request, 'Your rating has been added.')
    
    # Redirect back to the product details page
    return redirect('product_details', product_id=product_id)


@login_required
def remove_rating(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        rating = get_object_or_404(Rating, product=product, user=user)
        rating.delete()
        messages.success(request, 'Your rating has been removed.')

    return redirect('product_details', product_id=product_id)