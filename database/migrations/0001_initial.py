# Generated by Django 4.2.6 on 2023-11-15 14:58

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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='No asignado', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='No asignado', max_length=50)),
                ('cargo', models.CharField(choices=[('Gerente', 'Gerente'), ('Jefe', 'Jefe'), ('Coordinador', 'Coordinador'), ('Especialista', 'Especialista'), ('Supervisor', 'Supervisor'), ('Diseñador', 'Diseñador'), ('Programador', 'Programador'), ('Soporte', 'Soporte'), ('Analista', 'Analista')], default='Sin cargo', max_length=50)),
                ('cedula', models.IntegerField(default=0)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bien_nacional', models.CharField(default='000000', max_length=6)),
                ('marca', models.CharField(default='No asignado', max_length=50)),
                ('modelo', models.CharField(default='No asignado', max_length=50)),
                ('puertos', models.IntegerField(default=0)),
                ('ipv4', models.CharField(default='No asignado', max_length=50)),
                ('mac', models.CharField(default='No asignado', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bien_nacional', models.CharField(default='000000', max_length=6)),
                ('marca', models.CharField(default='No asignado', max_length=50)),
                ('modelo', models.CharField(default='No asignado', max_length=50)),
                ('puertos', models.IntegerField(default=0)),
                ('ipv4', models.CharField(default='No asignado', max_length=50)),
                ('mac', models.CharField(default='No asignado', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(default='No asignado', max_length=50)),
                ('bien_nacional', models.CharField(default='000000', max_length=6)),
                ('marca', models.CharField(default='No asignado', max_length=50)),
                ('modelo', models.CharField(default='No asignado', max_length=50)),
                ('ipv4', models.CharField(default='No asignado', max_length=50)),
                ('mac', models.CharField(default='No asignado', max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Solvencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bien_nacional', models.CharField(default='000000', max_length=6)),
                ('descripcion', models.CharField(default='No asignado', max_length=100)),
                ('marca', models.CharField(default='No asignado', max_length=50)),
                ('modelo', models.CharField(default='No asignado', max_length=50)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bien_nacional', models.CharField(default='000000', max_length=6)),
                ('marca', models.CharField(default='No asignado', max_length=50)),
                ('modelo', models.CharField(default='No asignado', max_length=50)),
                ('ipv4', models.CharField(default='No asignado', max_length=50)),
                ('mac', models.CharField(default='No asignado', max_length=50)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bien_nacional', models.CharField(default='000000', max_length=6)),
                ('marca', models.CharField(default='No asignado', max_length=50)),
                ('modelo', models.CharField(default='No asignado', max_length=50)),
                ('procesador', models.CharField(default='No asignado', max_length=50)),
                ('ram', models.IntegerField(default=0)),
                ('almacenamiento', models.IntegerField(default=0)),
                ('tipo_disco', models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], default='No asignado', max_length=50)),
                ('ipv4', models.CharField(default='No asignado', max_length=50)),
                ('mac', models.CharField(default='No asignado', max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Desincorporacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bien_nacional', models.CharField(default='000000', max_length=6)),
                ('descripcion', models.CharField(default='No asignado', max_length=100)),
                ('marca', models.CharField(default='No asignado', max_length=50)),
                ('modelo', models.CharField(default='No asignado', max_length=50)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.empleado')),
            ],
        ),
    ]
