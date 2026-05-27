from django.shortcuts import render,redirect
from .models import ProductModel,CartModel
# Create your views here.
def add_product(request):

    if request.method == "POST":

        p_name = request.POST.get('name')
        p_type = request.POST.get('type')
        p_price = request.POST.get('price')
        p_quantity = request.POST.get('quantity')

        ProductModel.objects.create(
            p_name=p_name,
            p_type=p_type,
            p_price=p_price,
            p_quantity=p_quantity
        )

        return render(request, 'success.html',
                      {"message": "Product added successfully"})

    return render(request, 'add_product.html')
def view_all_products(request):
    data=ProductModel.objects.all().values()
    print(list(data))
    return render(request, 'product_list.html',{'products': data})
def delete_product(request, id):

    product = ProductModel.objects.get(id=id)
    if request.method == "POST":
        product.delete()
        return redirect('/product/product_list/')
    return render(request, 'delete.html', {'product': product})
def update_product(request, id):
    product = ProductModel.objects.get(id=id)
    if request.method == "POST":
        product.p_name = request.POST.get('name')
        product.p_type = request.POST.get('type')
        product.p_price = request.POST.get('price')
        product.p_quantity = request.POST.get('quantity')
        product.save()
        return redirect('/product/product_list/')
    return render(request,
                  'update_product.html',
                  {'product': product})
def add_to_cart(request, id):
    product = ProductModel.objects.get(id=id)
    CartModel.objects.create(product=product)
    return redirect('/product/cart/')
def view_cart(request):
    cart_items = CartModel.objects.all()
    return render(request,
                  'cart.html',
                  {'cart_items': cart_items})
def remove_from_cart(request, id):
    item = CartModel.objects.get(id=id)
    item.delete()
    return redirect('/product/cart/')