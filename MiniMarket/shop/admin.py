from django.contrib import admin

# This changes the "Django Administration" text on the login page and top bar
admin.site.site_header = "Mini-Market Management"

# This changes the title in your Browser Tab
admin.site.site_title = "Mini-Market Admin Portal"

# This changes the "Site administration" text on the home page
admin.site.index_title = "Welcome to your Inventory Dashboard"

from .models import Product, Order

admin.site.register(Product)
admin.site.register(Order)