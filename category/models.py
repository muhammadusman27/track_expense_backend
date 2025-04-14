from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
# Create your models here.


class Category(models.Model):
    user = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.SET_NULL, db_column='user')
    name = models.CharField(max_length=255, null=False, db_column='name')
    description = models.TextField(blank=True, null=True, db_column='description')

    class Meta:
        db_table = 'Category'
        ordering = ['-id']