# Generated by Django 2.2.4 on 2019-08-12 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainn', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='fled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('me', models.CharField(max_length=30)),
                ('pw', models.CharField(max_length=30)),
                ('q', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kn.Fle')),
            ],
        ),
    ]
