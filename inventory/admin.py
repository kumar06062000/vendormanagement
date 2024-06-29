from django.contrib import admin


from django.contrib import admin
from .models import Vendor, Product, Comment, Rating

admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Rating)
