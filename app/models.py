import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Customer(models.Model):

    created             = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)
    name                = models.CharField(max_length=50)
    acquired_date       = models.DateField()
    retired_date        = models.DateField(blank=True, null=True)
    slug                = models.SlugField(unique=True, null=True, blank=True)
    external_uuid       = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Customer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Customer'

    def __str__(self):
        return self.name


class CustomerLocation(models.Model):
    created             = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=True)
    customer            = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address             = models.CharField(max_length=50)
    site_abbreviation   = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Customer Location'

    def __str__(self):
        return self.address


class JobStatus(models.Model):
    status              = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class Job(models.Model):
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    active              = models.BooleanField(default=True)
    status              = models.ForeignKey(JobStatus, on_delete=models.CASCADE)
    customer            = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_location   = models.ForeignKey(CustomerLocation, on_delete=models.CASCADE)
    scope_of_work       = models.CharField(max_length=100)
    request_from        = models.CharField(max_length=20)
    PO_number           = models.CharField(max_length=20)
    SC_work_order       = models.CharField(max_length=20)
    notes               = models.TextField(null=True, blank=True)
