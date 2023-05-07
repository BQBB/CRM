# Generated by Django 4.1.1 on 2023-04-05 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='quantity'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crmproject.user'),
        ),
    ]