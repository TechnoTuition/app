# Generated by Django 3.2.10 on 2021-12-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211223_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='default@email.com', max_length=245),
        ),
    ]