# Generated by Django 3.2a1 on 2021-05-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ensayo',
            fields=[
                ('id_ensayo', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('materia', models.CharField(max_length=50)),
                ('texto', models.TextField(max_length=50)),
            ],
        ),
    ]