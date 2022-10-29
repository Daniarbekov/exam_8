from django.views.generic import  CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Product
from django.urls import reverse, reverse_lazy
from webapp.forms import ProductForm
from django.contrib.auth.mixins import  UserPassesTestMixin



class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductCreate( UserPassesTestMixin,SuccessDetailUrlMixin, CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm
    model = Product
    
    def test_func(self):
        return self.request.user.has_perm('webapp.add_product')


class ProductView(DetailView):
    template_name = 'product/detail.html'
    model = Product
    

class ProductUpdateView( UserPassesTestMixin,SuccessDetailUrlMixin, UpdateView):
    template_name = 'product/update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    
    def test_func(self):
        return self.request.user.has_perm('webapp.change_product')


class ProductDeleteView( UserPassesTestMixin, DeleteView):
    template_name = 'product/confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    
    def test_func(self):
        return self.request.user.has_perm('webapp.delete_product')
