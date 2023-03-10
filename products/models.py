from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    short_description = RichTextField(verbose_name=_("Short Description"), blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_("Product Image"), upload_to='product/product_cover', blank=True)

    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_("Date And Time Created"))
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])


class Wishlist(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return str(self.user)


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    STAR_CHOICES = [
        ("1", _("Very Bad")),
        ("2", _("Bad")),
        ("3", _("Normal")),
        ("4", _("Good")),
        ("5", _("Perfect")),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',
                               verbose_name=_("Comment Author"))
    body = models.TextField(verbose_name=_("Comment Text"))
    stars = models.CharField(choices=STAR_CHOICES, max_length=10, verbose_name=_("What Is Your Score?"))
    active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True, verbose_name=_("Do you Recommend"))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
