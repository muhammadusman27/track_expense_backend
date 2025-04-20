from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=150, db_column='name')
    balance = models.FloatField(default=0, db_column='balance')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    user = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.SET_NULL, db_column='user')

    class Meta:
        ordering = ['-id']
        db_table = 'Account'
