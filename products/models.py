from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


# class ActiveCommentsManager(models.Manager):
#     def get_queryset(self):
#         return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'VERY BAD'),
        ('2', 'BAD'),
        ('1', 'NORMAL'),
        ('1', 'GOOD'),
        ('1', 'PERFECT'),
    ]
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments', )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', )
    body = models.TextField(verbose_name='Comment Text')
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS,verbose_name='Your Score',)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    # objects = models.BooleanField(default=True)
    # active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
