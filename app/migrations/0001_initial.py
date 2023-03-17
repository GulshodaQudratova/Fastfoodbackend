# Generated by Django 4.1.7 on 2023-03-12 20:26

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter name', max_length=150, null=True, verbose_name='BotUser name')),
                ('telegram_id', models.CharField(help_text='Enter telegram ID', max_length=20, unique=True, verbose_name='Telegram ID')),
                ('language', models.CharField(default='uz', help_text='Enter user language', max_length=5, verbose_name='User language')),
                ('phone', models.CharField(blank=True, help_text='Ënter user number', max_length=20, null=True, verbose_name='Phone number')),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'BotUser',
                'verbose_name_plural': 'BotUsers',
                'db_table': 'BotUser',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter category name', max_length=150, null=True, verbose_name='Category')),
                ('name_uz', models.CharField(blank=True, help_text='Enter category name', max_length=150, null=True, verbose_name='Category')),
                ('name_ru', models.CharField(blank=True, help_text='Enter category name', max_length=150, null=True, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'Category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.botuser', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'Order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter subcategory name', max_length=150, null=True, verbose_name='SubCategory')),
                ('name_uz', models.CharField(blank=True, help_text='Enter subcategory name', max_length=150, null=True, verbose_name='SubCategory')),
                ('name_ru', models.CharField(blank=True, help_text='Enter subcategory name', max_length=150, null=True, verbose_name='SubCategory')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='app.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'SubCategory',
                'verbose_name_plural': 'SubCategories',
                'db_table': 'SubCategory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter subcategory name', max_length=150, null=True, verbose_name='SubCategory')),
                ('name_uz', models.CharField(blank=True, help_text='Enter subcategory name', max_length=150, null=True, verbose_name='SubCategory')),
                ('name_ru', models.CharField(blank=True, help_text='Enter subcategory name', max_length=150, null=True, verbose_name='SubCategory')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product-images', verbose_name='Product image')),
                ('about', models.TextField(blank=True, help_text='Enter brief information about Product', null=True, verbose_name='Product outline')),
                ('about_uz', models.TextField(blank=True, help_text='Enter brief information about Product', null=True, verbose_name='Product outline')),
                ('about_ru', models.TextField(blank=True, help_text='Enter brief information about Product', null=True, verbose_name='Product outline')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Product price')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Product discount')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.category', verbose_name='Category')),
                ('subcategory', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='app.subcategory')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'Product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Product quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.order', verbose_name='Basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'OrderItems',
                'verbose_name_plural': 'OrderItems',
                'db_table': 'OrderItems',
                'managed': True,
            },
        ),
    ]