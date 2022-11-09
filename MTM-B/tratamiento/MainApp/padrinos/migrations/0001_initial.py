# Generated by Django 4.1.2 on 2022-10-25 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientexfamiliar', '0008_familiar_alter_eps_nit_alter_eps_numero_telefonico_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='donacion_padrino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_donacion', models.CharField(max_length=50, null=True, verbose_name='metodo de donacion')),
                ('tipo_donacion', models.CharField(max_length=50, null=True, verbose_name='tipo de donacion')),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='padrinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('nombre_padrino', models.CharField(max_length=50, null=True, verbose_name='Nombre del padrino')),
                ('apellido_padrino', models.CharField(max_length=50, null=True, verbose_name='apellido del padrino')),
                ('tipo_padrino', models.CharField(max_length=50, null=True, verbose_name='tipo de padrino')),
                ('sexo', models.CharField(max_length=50, null=True, verbose_name='sexo del padrino')),
                ('nivel_educativo', models.CharField(max_length=50, null=True, verbose_name='nivel educativo del padrino')),
                ('telefono', models.CharField(max_length=50, null=True, verbose_name='telefono del padrino')),
                ('direccion', models.CharField(max_length=50, null=True, verbose_name='direccion del padrino')),
                ('ciudad', models.CharField(max_length=50, null=True, verbose_name='ciudad del padrino')),
                ('departamento', models.CharField(max_length=50, null=True, verbose_name='departamento del padrino')),
                ('correo', models.CharField(max_length=50, null=True, verbose_name='correo del padrino')),
                ('tiempo_apradinando', models.CharField(max_length=50, null=True, verbose_name='tiempo apadrinado del padrino')),
                ('edad', models.PositiveIntegerField(default=0)),
                ('estrato', models.PositiveIntegerField(default=0)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente_x_padrino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientexfamiliar.paciente')),
                ('id_padrino', models.ManyToManyField(to='padrinos.padrinos')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente_x_donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('id_donacion', models.ManyToManyField(to='padrinos.donacion_padrino')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientexfamiliar.paciente')),
            ],
        ),
    ]