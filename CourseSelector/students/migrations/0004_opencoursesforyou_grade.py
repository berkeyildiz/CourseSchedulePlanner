# Generated by Django 2.2.1 on 2019-05-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20190513_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='opencoursesforyou',
            name='grade',
            field=models.CharField(default=None, max_length=5, null=True),
        ),
    ]
