# inventory/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Vendor, Product, Comment, Rating
from .forms import VendorForm, ProductForm, CommentForm, RatingForm, UserRegisterForm
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()
    return render(request, 'inventory/home.html', {'products': products, 'query': query})
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'inventory/register.html', {'form': form})

@login_required
def vendor_dashboard(request):
    vendor = get_object_or_404(Vendor, user=request.user)
    products = vendor.products.all()
    return render(request, 'inventory/vendor_dashboard.html', {'vendor': vendor, 'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = Vendor.objects.get(user=request.user)
            product.save()
            messages.success(request, 'Product added successfully.')
            return redirect('vendor_dashboard')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, vendor__user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('vendor_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, vendor__user=request.user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('vendor_dashboard')
    return render(request, 'inventory/delete_product.html', {'product': product})

@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('product_detail', product_id=product_id)
    else:
        form = CommentForm()
    return render(request, 'inventory/add_comment.html', {'form': form, 'product': product})

@login_required
def add_rating(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.product = product
            rating.user = request.user
            rating.save()
            messages.success(request, 'Rating added successfully.')
            return redirect('product_detail', product_id=product_id)
    else:
        form = RatingForm()
    return render(request, 'inventory/add_rating.html', {'form': form, 'product': product})

@staff_member_required
def add_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = User.objects.create_user(username=form.cleaned_data['company_name'])
            vendor.save()
            messages.success(request, 'Vendor added successfully.')
            return redirect('admin_dashboard')
    else:
        form = VendorForm()
    return render(request, 'inventory/add_vendor.html', {'form': form})

@staff_member_required
def edit_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES, instance=vendor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendor updated successfully.')
            return redirect('admin_dashboard')
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'inventory/edit_vendor.html', {'form': form})

@staff_member_required
def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        vendor.delete()
        messages.success(request, 'Vendor deleted successfully.')
        return redirect('admin_dashboard')
    return render(request, 'inventory/delete_vendor.html', {'vendor': vendor})

@staff_member_required
def admin_dashboard(request):
    vendors = Vendor.objects.all()
    return render(request, 'inventory/admin_dashboard.html', {'vendors': vendors})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = product.comments.all()
    ratings = product.ratings.all()
    return render(request, 'inventory/product_detail.html', {
        'product': product,
        'comments': comments,
        'ratings': ratings
    })
