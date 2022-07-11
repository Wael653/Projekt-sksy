
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
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nummer', models.CharField(max_length=15, verbose_name='Nummer')),
            ],
        ),
        migrations.CreateModel(
            name='RoomDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=160, verbose_name='Bezeichnung')),
                ('anzahl', models.PositiveIntegerField(default=1, verbose_name='Anzahl')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('straße', models.CharField(default='Straße des 17. Juni', max_length=50, verbose_name='Straße')),
                ('hausnummer', models.CharField(default='135', max_length=10, verbose_name='Hausnummer')),
                ('postleitzahl', models.CharField(default='10623', max_length=5, verbose_name='Postleitzahl')),
                ('etage', models.IntegerField(default=0, verbose_name='Etage')),
            ],
        ),
        migrations.CreateModel(
            name='WorkplaceDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=160, verbose_name='Bezeichnung')),
                ('anzahl', models.PositiveIntegerField(default=1, verbose_name='Anzahl')),
            ],
            options={
                'ordering': ['nummer'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nummer', models.PositiveIntegerField()),
                ('anzahlPersonen', models.PositiveIntegerField(default=1)),
                ('sonstiges', models.CharField(blank=True, max_length=160, null=True)),
                ('barrierefrei', models.BooleanField(blank=True, default=True, null=True, verbose_name='Barrierefrei')),
                ('geraete', models.ManyToManyField(blank=True, to='starsApp.workplacedevice')),
                ('raum', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='starsApp.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='geraete',
            field=models.ManyToManyField(to='starsApp.roomdevice'),
        ),
        migrations.AddField(
            model_name='room',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='starsApp.unit'),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('von', models.DateTimeField()),
                ('bis', models.DateTimeField()),
                ('sonstiges', models.CharField(blank=True, max_length=160, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('wp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='starsApp.workplace')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]
