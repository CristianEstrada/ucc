# Generated by Django 4.0.4 on 2022-10-20 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientexfamiliar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente_x_estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientexfamiliar.estado')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientexfamiliar.paciente')),
            ],
        ),
    ]
