# Generated by Django 4.2.7 on 2023-12-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_student_date_of_birth_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, upload_to='albums/'),
        ),
    ]
