# Generated by Django 3.1.1 on 2020-09-27 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requirement', '0004_auto_20200926_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirementmodel',
            name='Category',
        ),
        migrations.AddField(
            model_name='requirementmodel',
            name='category',
            field=models.CharField(choices=[('Medicines', 'Medicines'), ('Ventilators', 'Ventilators'), ('Beds', 'Beds'), ('Other', 'Other')], default='Medicines', max_length=20),
        ),
        migrations.AddField(
            model_name='requirementmodel',
            name='ngo_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DonationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=20)),
                ('quantity_donated', models.CharField(max_length=20)),
                ('donated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('doner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
