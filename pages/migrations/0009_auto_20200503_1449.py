# Generated by Django 3.0.4 on 2020-05-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_promotion_email_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion_email_list',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
