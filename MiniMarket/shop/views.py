from django.shortcuts import render
from .models import Product

def home(request):
    query = request.GET.get('q') # Get the search query
    category_name = request.GET.get('category')
    
    if query:
        # Search for products by name
        products = Product.objects.filter(name__icontains=query)
    elif category_name:
        products = Product.objects.filter(category=category_name)
    else:
        products = Product.objects.all()
    
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    return render(request, 'shop/index.html', {
        'products': products, 
        'categories': categories,
        'query': query
    })
def checkout(request):
    if request.method == "POST":
        # Get data from the form
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        total_price = request.POST.get('total_price', 0)

        # Save to Database
        order = Order.objects.create(
            full_name=full_name,
            phone=phone,
            address=address,
            total_price=total_price
        )
        return render(request, 'shop/success.html', {'order': order})
    
    return render(request, 'shop/checkout.html')