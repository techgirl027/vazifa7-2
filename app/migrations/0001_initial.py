# Generated by Django 5.0.7 on 2024-07-29 13:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generete_code', models.CharField(blank=True, max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(upload_to='banners/')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generete_code', models.CharField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generete_code', models.CharField(blank=True, max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generete_code', models.CharField(blank=True, max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('shopping_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generete_code', models.CharField(blank=True, max_length=255, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=255)),
                ('status', models.SmallIntegerField(choices=[(1, 'Tayyorlanmoqda'), (2, 'Yo`lda'), (3, 'Yetib borgan'), (4, 'Qabul qilingan'), (5, 'Qaytarilgan')])),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cart')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generete_code', models.CharField(blank=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generete_code', models.CharField(blank=True, max_length=255, unique=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cart')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductEnter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generete_code', models.CharField(blank=True, max_length=255, unique=True)),
                ('quantitiy', models.IntegerField()),
                ('old_quantity', models.IntegerField(blank=True)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generete_code', models.CharField(blank=True, max_length=255, unique=True)),
                ('img', models.ImageField(upload_to='product-img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
