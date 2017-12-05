from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    phone = models.CharField(null=True, max_length=255)
    zip_code = models.CharField(null=True, max_length=6)
    pin = models.CharField(null=True, max_length=4)
    approved = models.BooleanField(default=False)
    amount_invested = models.DecimalField(default='0.00', max_digits=12, decimal_places=2)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
