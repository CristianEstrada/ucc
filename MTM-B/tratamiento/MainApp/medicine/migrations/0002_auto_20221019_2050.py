# Generated by Django 3.2 on 2022-10-19 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medication_formula',
            field=models.CharField(max_length=50, null=True, verbose_name='Formula del medicamento'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medication_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre del medicine'),
        ),
    ]
