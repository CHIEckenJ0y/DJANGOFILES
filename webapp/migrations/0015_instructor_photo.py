# Generated by Django 4.2.7 on 2024-01-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_remove_student_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='photo',
            field=models.ImageField(blank=True, upload_to='albums/'),
        ),
    ]
