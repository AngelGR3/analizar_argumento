# Generated by Django 3.2a1 on 2021-10-11 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensayo', '0015_ensayo_promedio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ensayo',
            name='mar_valorconclu',
            field=models.CharField(default='0', max_length=10000),
        ),
        migrations.AlterField(
            model_name='ensayo',
            name='mar_valorpremisa',
            field=models.CharField(default='0', max_length=10000),
        ),
    ]
