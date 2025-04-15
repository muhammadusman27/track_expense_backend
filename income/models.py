from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
# Create your models here.

class Income(models.Model):
    name = models.CharField(max_length=150, null=False, db_column='name')
    description = models.TextField(null=True, blank=True, db_column='description')
    date = models.DateField(null=False, db_column='date')
    amount = models.FloatField(null=False, db_column='amount')
    user = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.SET_NULL, db_column='user')
    

    class Meta:
        ordering = ['-id']