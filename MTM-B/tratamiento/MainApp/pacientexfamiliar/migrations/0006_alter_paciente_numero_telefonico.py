# Generated by Django 4.0.4 on 2022-10-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientexfamiliar', '0005_alter_paciente_numero_telefonico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='numero_telefonico',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
