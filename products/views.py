from django.shortcuts import render
from django.views import generic

from .forms import CommentForm
from .models import Products, Comment


class ProductListView(generic.ListView):
    # model = Products
    queryset = Products.objects.filter(active=True)
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super().form_valid(form)
