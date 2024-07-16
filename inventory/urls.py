from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/product/add/', views.add_product, name='add_product'),
    path('vendor/product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('vendor/product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/comment/add/', views.add_comment, name='add_comment'),
    path('product/<int:product_id>/rating/add/', views.add_rating, name='add_rating'),
    path('admin_panel/vendor/add/', views.add_vendor, name='add_vendor'),
    path('admin_panel/vendor/edit/<int:vendor_id>/', views.edit_vendor, name='edit_vendor'),
    path('admin_panel/vendor/delete/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),
    path('admin_panel/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    
    path('generate_excel_report/', views.generate_excel_report, name='generate_excel_report'),
    path('update_notification_preference/', views.update_notification_preference, name='update_notification_preference'),
    path('set_review_interval/', views.set_review_interval, name='set_review_interval'),
]
