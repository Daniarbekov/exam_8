from django.urls import path
from webapp.views.base import IndexView
from webapp.views.products import ProductCreate, ProductView, ProductUpdateView, ProductDeleteView
from webapp.views.reviews import ReviewCreate, ReviewUpdateView


urlpatterns= [
    path("", IndexView.as_view(), name='index'),
    path('products/add', ProductCreate.as_view(), name='product_add'),
    path('product/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/add_review', ReviewCreate.as_view(), name='add_review'),
    path('product/<int:pk>/review/update', ReviewUpdateView.as_view(), name='update_review')
]
