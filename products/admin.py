from django.contrib import admin

from .models import Products, Comment


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active', ]
