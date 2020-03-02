from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by =models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.client_name