# Generated by Django 4.2.6 on 2023-10-31 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cargo', models.CharField(choices=[('Gerente', 'Gerente'), ('Jefe', 'Jefe'), ('Coordinador', 'Coordinador'), ('Especialista', 'Especialista'), ('Supervisor', 'Supervisor'), ('Diseñador', 'Diseñador'), ('Programador', 'Programador'), ('Soporte', 'Soporte'), ('Analista', 'Analista')], default='Sin cargo', max_length=50)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('puertos', models.IntegerField(default=0)),
                ('ipv4', models.CharField(max_length=50)),
                ('mac', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('puertos', models.IntegerField(default=0)),
                ('ipv4', models.CharField(max_length=50)),
                ('mac', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('ipv4', models.CharField(max_length=50)),
                ('mac', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('procesador', models.CharField(max_length=50)),
                ('ram', models.IntegerField(default=0)),
                ('almacenamiento', models.IntegerField(default=0)),
                ('tipo_disco', models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=50)),
                ('ipv4', models.CharField(max_length=50)),
                ('mac', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.empleado')),
            ],
        ),
    ]
