# Generated by Django 4.2.7 on 2023-11-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='decs',
            new_name='desc',
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(blank=True),
        ),
    ]