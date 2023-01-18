from django.contrib import admin

from .models import Products, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active', ]


