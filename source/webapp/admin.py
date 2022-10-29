from django.contrib import admin
from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category','image')
    list_filter = ('id', 'name', 'description', 'category','image')
    search_fields = ('category', 'name')

admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author','product','rating', 'text')
    list_filter = ('id', 'author','product', 'rating', 'text')

admin.site.register(Review, ReviewAdmin)
    