# Generated by Django 2.0.3 on 2018-06-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahm', '0004_monitoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitoria',
            name='materia',
        ),
        migrations.AddField(
            model_name='monitor',
            name='materia',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
