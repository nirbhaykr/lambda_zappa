from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.


class Transcation(models.Model):
    """
        Model for Transaction mapping
    """
    product = models.CharField(max_length=255, default=None, blank=True, null= True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    line_total = models.FloatField(blank=True, null=True, default=0)

    def __unicode__(self):
        return self.product


class Invoice(models.Model):
    """
        Model for storing Invoice data
    """
    custumer = models.CharField(max_length=255, default=None, blank=True, null= True)
    invoice_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    transaction = models.ManyToManyField(Transcation)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=Transcation)
def Update_line_total(sender, instance=None, created=False, **kwargs):
    if created:
        instance.line_total = instance.price * instance.quantity
        instance.save()

