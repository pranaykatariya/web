# Generated by Django 3.0.4 on 2020-04-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_slambook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slambook',
            name='advice',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='dislike',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='like',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='similar_things',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='song',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='slambook',
            name='sweet_memory',
            field=models.TextField(),
        ),
    ]
