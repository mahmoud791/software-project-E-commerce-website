# Generated by Django 3.1.4 on 2020-12-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201218_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(auto_created=models.CharField(max_length=200, null=True), null=True, unique=True),
        ),
    ]
