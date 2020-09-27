# Generated by Django 3.1.1 on 2020-09-27 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requirement', '0005_auto_20200927_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationmodel',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='requirement.requirementmodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requirementmodel',
            name='ngo_name',
            field=models.CharField(default='fehjrj', editable=False, max_length=20),
        ),
    ]
