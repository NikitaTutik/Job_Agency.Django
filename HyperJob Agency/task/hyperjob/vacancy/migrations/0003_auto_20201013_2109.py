# Generated by Django 2.2 on 2020-10-13 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_delete_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
