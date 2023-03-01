from django.db import models
from django.contrib.auth.models import Group


class MyModel(models.Model):
    # Fields
    # ...

    class Meta:
        permissions = (
            ('can_do_something', 'Can do something'),
            ('can_do_another_thing', 'Can do another thing'),
        )
