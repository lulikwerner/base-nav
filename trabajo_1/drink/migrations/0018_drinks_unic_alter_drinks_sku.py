# Generated by Django 4.0.6 on 2022-08-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0017_alter_drinks_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='unic',
            field=models.CharField(default='d', max_length=1),
        ),
        migrations.AlterField(
            model_name='drinks',
            name='sku',
            field=models.IntegerField(default=1263),
        ),
    ]
