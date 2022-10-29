from django.views.generic import ListView
from webapp.models import Product, Review


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'

