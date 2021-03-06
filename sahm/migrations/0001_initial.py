# Generated by Django 2.0.3 on 2018-03-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('matricula', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.BigIntegerField()),
                ('curso', models.CharField(max_length=200)),
                ('periodo', models.PositiveSmallIntegerField()),
                ('nascimento', models.DateField()),
                ('senha', models.CharField(max_length=200)),
            ],
        ),
    ]
