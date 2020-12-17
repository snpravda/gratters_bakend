# Generated by Django 3.1.4 on 2020-12-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gratters', '0004_delete_gratter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gratter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('person_to', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
