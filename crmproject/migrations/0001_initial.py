# Generated by Django 4.1.1 on 2023-04-05 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('address1', models.CharField(max_length=255, verbose_name='address1')),
                ('address2', models.CharField(max_length=255, verbose_name='address2')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='phone')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('price', models.FloatField(verbose_name='price')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='quantity')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=36, verbose_name='password')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='phone')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField(verbose_name='cost')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmproject.address')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmproject.product')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmproject.user'),
        ),
    ]