from django.db import models
from django.conf import settings
from django.urls import reverse

class TLD(models.Model):
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name


class Domain(models.Model):
    ip_address = models.CharField(max_length=15, null=False)
    names = models.TextField(null=False)
    TLD = models.ForeignKey(TLD, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=None, null=True, blank=True)
    verified_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.ip_address
    
    def get_absolute_url(self):
        return reverse('domain-detail', args=[str(self.id)])


class SubDomain(models.Model):
    ip_address = models.CharField(max_length=200, null=False)
    names = models.TextField(null=False)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.ip_address