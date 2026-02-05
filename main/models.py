from django.db import models


class Specification(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to="products/", blank=True, null=True)

    is_new = models.BooleanField(default=False)
    is_hit = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)

    specifications = models.ManyToManyField(Specification, blank=True)

    def __str__(self):
        return self.name