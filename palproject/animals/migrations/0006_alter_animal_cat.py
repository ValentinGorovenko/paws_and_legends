# Generated by Django 4.2.1 on 2024-09-11 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0005_category_animal_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animals.category'),
        ),
    ]
