# Generated by Django 2.2.1 on 2019-05-15 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20190515_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='allopencourses',
            name='coreq',
            field=models.CharField(default='girilmemis', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='opencoursesforyou',
            name='coreq',
            field=models.CharField(default='girilmemis', max_length=10, null=True),
        ),
    ]