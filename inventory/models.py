from django.db import models
from .utils import uuid_upload_to
class Account(models.Model):
    name = models.CharField(max_length=25)
    call = models.CharField(max_length=18)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to=uuid_upload_to)
    content = models.TextField()
    price = models.IntegerField()
    amount = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def amount_count(self):
        return self.amount.count()

