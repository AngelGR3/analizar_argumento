# Generated by Django 3.2a1 on 2021-09-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensayo', '0006_auto_20210913_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ensayo',
            name='mar_conclu',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='ensayo',
            name='mar_premisa',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='ensayo',
            name='mar_valorconclu',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='ensayo',
            name='mar_valorpremisa',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
