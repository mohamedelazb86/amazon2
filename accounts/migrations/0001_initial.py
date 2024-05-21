# Generated by Django 4.2 on 2024-05-21 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.generate_code


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_user')),
                ('code', models.CharField(default=utils.generate_code.generate_code, max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
