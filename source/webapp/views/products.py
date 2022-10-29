from django.views.generic import  CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Product
from django.urls import reverse, reverse_lazy
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
    

class ProductUpdateView(SuccessDetailUrlMixin, UpdateView):
    template_name = 'product/update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    template_name = 'product/confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
