# Generated by Django 4.0.6 on 2022-08-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0006_alter_drinks_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='sku',
            field=models.IntegerField(default=525),
        ),
    ]
