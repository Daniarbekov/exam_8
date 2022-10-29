from django.views.generic import  CreateView, DetailView
from webapp.models import Product
from django.urls import reverse
from webapp.forms import ProductForm

class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductCreate(SuccessDetailUrlMixin, CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm
    model = Product


class ProductView(DetailView):
    template_name = 'product/detail.html'
    model = Product