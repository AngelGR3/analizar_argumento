# Generated by Django 3.2a1 on 2021-10-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensayo', '0011_alter_ensayo_promedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ensayo',
            name='promedia',
            field=models.FloatField(max_length=300),
        ),
    ]
