# Generated by Django 3.1.6 on 2021-02-18 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210218_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', unique=True),
        ),
    ]
