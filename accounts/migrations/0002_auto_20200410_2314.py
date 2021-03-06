# Generated by Django 3.0.4 on 2020-04-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_credentials',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='achievement',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='bed',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='company',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='distract',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='evening',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='fear',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='gender',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='happy',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='insta_username',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='job',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='lastname',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='mobile',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='occupation',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='risk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='rule',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user_credentials',
            name='wish',
            field=models.TextField(null=True),
        ),
    ]
