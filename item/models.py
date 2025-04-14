from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255, null=False, db_column='name')
    description = models.TextField(null=True, db_column='description')
    category = models.ForeignKey('category.Category', on_delete=models.SET_NULL, null=True, db_column='category')
    user = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.SET_NULL, db_column='user')

    class Meta:
        db_table = 'Item'
        ordering = ['-id']