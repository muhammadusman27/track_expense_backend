from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
# Create your models here.

class Expense(models.Model):
    item = models.ForeignKey('item.Item', on_delete=models.SET_NULL, null=True, db_column='item')
    category = models.ForeignKey('category.Category', on_delete=models.SET_NULL, null=True, db_column='category')
    account = models.ForeignKey(to='account.Account', null=True, blank=True, on_delete=models.SET_NULL, db_column='account')
    quantity = models.IntegerField(default=None, null=True, db_column='quantity')
    name = models.CharField(max_length=255, db_column='name')
    description = models.TextField(null=True, blank=True, db_column='description')
    price = models.IntegerField(null=False, db_column='price')
    weight = models.FloatField(default=None, null=True, db_column='weight')
    weight_unit = models.CharField(choices=[('kg', 'kg'), ('g', 'g'), ('ml', 'ml')], null=True, default=None, db_column='weight_unit', max_length=5)
    date = models.DateField(db_column='date')
    user = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.SET_NULL, db_column='user')


    class Meta:
        db_table = 'Expense'
        ordering = ['-id']
