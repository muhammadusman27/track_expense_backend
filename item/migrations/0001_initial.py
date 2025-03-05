# Generated by Django 5.1.6 on 2025-03-05 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('description', models.TextField(db_column='description', null=True)),
                ('category', models.ForeignKey(db_column='category', null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
            ],
            options={
                'db_table': 'Item',
                'ordering': ['-id'],
            },
        ),
    ]
