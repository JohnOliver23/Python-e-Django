# Generated by Django 2.1.3 on 2018-11-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('horario', models.DateTimeField()),
                ('lab', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
    ]
