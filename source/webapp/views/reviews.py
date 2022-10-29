from itertools import product
from django.views.generic import  CreateView, UpdateView, DeleteView
from webapp.forms import ReviewForm
from webapp.models import Review, Product
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import  UserPassesTestMixin, LoginRequiredMixin


class ReviewCreate(LoginRequiredMixin, CreateView):
    template_name = 'review/review_create.html'
    form_class = ReviewForm
    model = Review
    
    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.product = product
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.kwargs.get('pk')})


class ReviewUpdateView(UserPassesTestMixin,UpdateView): 
    model = Review
    template_name = 'review/update.html'
    form_class = ReviewForm
    
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.get_object().product.pk})
    
    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perms('webapp.delete_review', 'webapp.change_review')


class ReviewDeleteView(UserPassesTestMixin,DeleteView):
    template_name = 'review/delete_confirm.html'
    model = Review
    
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.get_object().product.pk})
    
    def test_func(self):
        return self.request.user.has_perms('webapp.delete_review', 'webapp.change_review')
