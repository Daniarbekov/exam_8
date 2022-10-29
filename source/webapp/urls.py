from django.urls import path
from webapp.views.base import IndexView
from webapp.views.products import ProductCreate, ProductView, ProductUpdateView


urlpatterns= [
    path("", IndexView.as_view(), name='index'),
    path('products/add', ProductCreate.as_view(), name='product_add'),
    path('product/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update')
]