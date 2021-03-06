# Generated by Django 3.0.6 on 2020-05-14 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('dpi', models.IntegerField(verbose_name='DPI')),
                ('nit', models.IntegerField(verbose_name='NIT')),
                ('tarjeta', models.IntegerField()),
                ('clave', models.IntegerField(verbose_name='Clave')),
                ('fecha_tarjeta', models.DateField(verbose_name='Vencimiento')),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]
