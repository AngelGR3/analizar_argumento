# Generated by Django 3.2a1 on 2021-10-03 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensayo', '0013_rename_promedia_ensayo_promedio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ensayo',
            name='promedio',
        ),
    ]