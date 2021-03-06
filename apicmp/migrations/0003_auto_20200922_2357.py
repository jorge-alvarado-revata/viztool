# Generated by Django 3.0 on 2020-09-22 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apicmp', '0002_pais_pesou_programau_universidad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterField(
            model_name='programau',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='programau',
            name='universidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apicmp.Universidad'),
        ),
    ]
