# Generated by Django 4.2.7 on 2023-12-02 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_course_enrollment_student_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='grade',
            new_name='year_level',
        ),
    ]
