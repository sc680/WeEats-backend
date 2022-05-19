<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-05-18 01:59
=======
# Generated by Django 4.0.4 on 2022-05-18 13:05
>>>>>>> c141d2a (Add : login test)

from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('restaurants', '0001_initial'),
        ('users', '0001_initial'),
=======
        ('users', '0001_initial'),
        ('restaurants', '0001_initial'),
>>>>>>> c141d2a (Add : login test)
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'reservation_statuses',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('timeslot', models.IntegerField(choices=[(1, '12:00 - 14:00'), (2, '14:00 - 16:00'), (3, '16:00 - 18:00'), (4, '18:00 - 20:00'), (5, '20:00 - 22:00')])),
                ('visitor_count', models.PositiveIntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservationstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'reservations',
            },
        ),
        migrations.AddConstraint(
            model_name='reservation',
            constraint=models.UniqueConstraint(fields=('restaurant', 'date', 'timeslot'), name='unique_reservation'),
        ),
    ]