# Generated by Django 4.2.6 on 2023-11-09 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_alter_departamento_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='desincorporacion',
            old_name='equipo',
            new_name='asignado',
        ),
    ]
