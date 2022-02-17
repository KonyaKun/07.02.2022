# Generated by Django 3.0 on 2022-02-14 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_auto_20220211_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='datetime_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время удаления'),
        ),
        migrations.AddField(
            model_name='account',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
        migrations.AddField(
            model_name='professor',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='datetime_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время удаления'),
        ),
        migrations.AddField(
            model_name='professor',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
        migrations.AddField(
            model_name='student',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='datetime_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время удаления'),
        ),
        migrations.AddField(
            model_name='student',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
    ]