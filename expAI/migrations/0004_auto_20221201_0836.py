# Generated by Django 3.2 on 2022-12-01 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expAI', '0003_auto_20221201_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='usrclass',
        ),
        migrations.AddField(
            model_name='user',
            name='usrclass',
            field=models.ManyToManyField(blank=True, db_column='usrclass', null=True, to='expAI.Class'),
        ),
    ]