# Generated by Django 4.2 on 2024-05-27 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.generate_code


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_address'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('completed', 'completed'), ('inprogress', 'inprogress')], max_length=50)),
                ('total_with_copoun', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Copoun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('start_date', models.DateField(verbose_name=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('quantity', models.FloatField()),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Recieved', 'Recieved'), ('Processed', 'Processed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=50)),
                ('code', models.CharField(default=utils.generate_code.generate_code, max_length=50)),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivery_time', models.DateTimeField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('total_with_copoun', models.FloatField(blank=True, null=True)),
                ('copoun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_copoun', to='orders.copoun')),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_address', to='accounts.address')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('total', models.FloatField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detatil_order', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail_product', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('total', models.FloatField(blank=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detatil_cart', to='orders.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_detail_product', to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='copoun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_copoun', to='orders.copoun'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
