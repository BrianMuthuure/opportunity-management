from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='logos', default='default.png')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('account-detail', kwargs={'pk': self.pk})


class Opportunity(models.Model):
    STAGE = (
        ('Discovery', 'Discovery'),
        ('Proposal Shared', 'Proposal Shared'),
        ('Negotiations', 'Negotiations'),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.PositiveSmallIntegerField(default=1)
    stage = models.CharField(choices=STAGE, max_length=150)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'opportunities'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('opportunity-detail', kwargs={'pk': self.pk})
