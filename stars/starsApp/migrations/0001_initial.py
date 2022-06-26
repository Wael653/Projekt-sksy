# Generated by Django 4.0.4 on 2022-06-26 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nummer', models.PositiveIntegerField()),
                ('geraete', models.CharField(max_length=160, null=True)),
                ('anzahlPersonen', models.PositiveIntegerField(default=1)),
                ('sonstiges', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('von', models.DateTimeField()),
                ('bis', models.DateTimeField()),
                ('sonstiges', models.CharField(max_length=160, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('wp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='starsApp.workplace')),
            ],
        ),
    ]
