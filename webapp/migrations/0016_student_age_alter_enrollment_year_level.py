# Generated by Django 4.2.7 on 2024-01-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_instructor_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='year_level',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
    ]