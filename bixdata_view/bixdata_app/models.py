from django.contrib.auth.models import AbstractUser
from django.contrib.auth.views import LoginView
from django.db import models


class MyModel(models.Model):
    class Meta:
        permissions = (
            ('can_do_something', 'Can do something'),
            ('can_do_another_thing', 'Can do another thing'),
        )


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomUser(AbstractUser):
    description = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_users',
        related_query_name='custom_user',
    )