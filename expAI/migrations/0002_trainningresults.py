# Generated by Django 3.2.2 on 2022-12-15 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expAI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainningresults',
            fields=[
                ('trainresultid', models.AutoField(db_column='trainResultID', primary_key=True, serialize=False)),
                ('trainresultindex', models.IntegerField(db_column='trainResultIndex', default=0)),
                ('lossvalue', models.FloatField(db_column='lossvalue')),
                ('accuracy', models.FloatField(db_column='accuracy')),
                ('configid', models.ForeignKey(blank=True, db_column='configID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.paramsconfigs')),
            ],
        ),
    ]
