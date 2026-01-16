from django.shortcuts import render, redirect
from .models import Sale, SaleItem
from products.models import Product
# Create your views here.
def create_sale(request):
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(id=product_id)

        sale = Sale.objects.create()

        SaleItem.objects.create(
            sale = sale,
            product = product,
            quantity =quantity,
            price = product.price
        )

        product.stock -= quantity
        product.save()

        return redirect('create_sale')

    return render(request, 'sales/create_sale.html', {
    'products': products
    })