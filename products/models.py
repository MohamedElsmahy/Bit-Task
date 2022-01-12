from django.db import models

from accounts.models import User

# Create your models here.


class Product(models.Model):
    class Meta:
        ordering = ["-price"]

    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=0)
    seller = models.ForeignKey(
        User, related_name='product_owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
