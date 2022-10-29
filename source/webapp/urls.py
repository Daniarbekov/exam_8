from django.urls import path
from webapp.views.base import IndexView
from webapp.views.products import ProductCreate, ProductView


urlpatterns= [
    path("", IndexView.as_view(), name='index'),
    path('products/add', ProductCreate.as_view(), name='product_add'),
    path('product/<int:pk>', ProductView.as_view(), name='product_detail')
]