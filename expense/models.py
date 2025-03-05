from django.db import models

# Create your models here.

class Expense(models.Model):
    item = models.ForeignKey('item.Item', on_delete=models.SET_NULL, null=True, db_column='item')
    quantity = models.IntegerField(default=None, null=True, db_column='quantity')
    description = models.TextField(null=True, db_column='description')
    price = models.IntegerField(null=False, db_column='price')
    weight = models.FloatField(default=None, null=True, db_column='weight')
    weight_unit = models.CharField(choices=[('kg', 'kg'), ('g', 'g'), ('ml', 'ml')], null=True, default=None, db_column='weight_unit', max_length=5)
    date = models.DateField(db_column='date')


    class Meta:
        db_table = 'Expense'
        ordering = ['-id']
