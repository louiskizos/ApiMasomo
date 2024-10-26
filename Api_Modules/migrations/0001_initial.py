# Generated by Django 4.2.16 on 2024-10-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etablissements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('designationEcole', models.TextField()),
                ('arreteMin', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('telephone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('typesEcole', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('biographie', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typesEcole', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
            ],
        ),
    ]