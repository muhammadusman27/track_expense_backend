from django.db import models

# Create your models here.


class Category(models.Model):
    user = models.ForeignKey(to="user_management.User", null=True, blank=True, on_delete=models.SET_NULL, db_column='user')
    name = models.CharField(max_length=255, null=False, db_column='name')
    description = models.TextField(null=True, db_column='description')


    class Meta:
        db_table = 'Category'
        ordering = ['-id']