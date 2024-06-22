from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm


# Create your views here.
def create_list(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "main/create.html", {"form": form})


def product_list(request):
    products = Product.objects.all()
    return render(request, "main/index.html", {"products": products})


def product_detail(request, pk):
    products = Product.objects.get(pk=pk)
    return render(request, "main/index2.html", {"products": products})


def edit_product(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "main/edit.html", {"form": form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "main/delete.html", {"product": product})


def home(request):
    return HttpResponse("Hello, World!")
