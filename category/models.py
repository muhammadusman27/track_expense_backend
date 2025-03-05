from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, db_column='name')
    description = models.TextField(null=True, db_column='description')


    class Meta:
        db_table = 'Category'
        ordering = ['-id']