# Generated by Django 2.2.1 on 2019-05-15 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_opencoursesforyou_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='opencoursesforyou',
            name='elective',
            field=models.CharField(default=None, max_length=25, null=True),
        ),
    ]
