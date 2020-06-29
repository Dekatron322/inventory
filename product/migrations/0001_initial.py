# Generated by Django 2.2.13 on 2020-06-28 20:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cost_price', models.IntegerField()),
                ('selling_price', models.IntegerField(blank=True, null=True)),
                ('expiry_date', models.CharField(max_length=150)),
                ('product_id', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SoldProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cost_price', models.IntegerField(blank=True, null=True)),
                ('selling_price', models.IntegerField(blank=True, null=True)),
                ('expiry_date', models.CharField(max_length=150)),
                ('product_id', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]