# Generated by Django 3.0 on 2020-09-24 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apicmp', '0005_auto_20200923_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peso',
            name='programa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pesos', to='apicmp.Programa'),
        ),
    ]