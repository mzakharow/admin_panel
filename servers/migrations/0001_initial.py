# Generated by Django 2.0.2 on 2018-02-28 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Server1C',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=256)),
                ('port', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servers.Port')),
            ],
        ),
    ]
