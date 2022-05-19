from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Restaurant_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail_image', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'restaurant_images',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('detail_image', models.CharField(max_length=500)),
                ('max_capacity', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.category')),
                ('thumbnail_image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant_image')),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
    ]
