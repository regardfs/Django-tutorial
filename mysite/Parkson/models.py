from django.db import models

# Create your models here.

class Parkson(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, verbose_name='PhoneNum')
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3,decimal_places=0)
    numbers = models.DecimalField(max_digits=2,decimal_places=0)
    favourite = models.BooleanField()
    restaurant = models.ForeignKey(Parkson)

    pungency_degree_choices = (
        ('不辣', '不辣'),
        ('微辣', '微辣'),
        ('中辣', '中辣'),
        ('非常辣', ' 非常辣'),
    )

    pungency_degree = models.CharField(
        max_length=20,
        choices=pungency_degree_choices,
        default='不辣',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['price']


class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Parkson)