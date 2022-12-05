# Generated by Django 3.2 on 2022-12-04 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expAI', '0005_auto_20221201_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasets',
            name='datasetproblem',
        ),
        migrations.AddField(
            model_name='datasets',
            name='datasetsoftID',
            field=models.ForeignKey(blank=True, db_column='datasetsoftID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.softwarelibs'),
        ),
        migrations.AlterField(
            model_name='softwarelibs',
            name='softwarelibid',
            field=models.AutoField(db_column='softwarelibID', primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Problem',
        ),
        migrations.RunSQL('INSERT INTO `softwarelibs` (`softwarelibName`, `softwarelibURL`) VALUES ("Thư viện Nhận diện khuôn mặt", "FACE_REG");'),
        migrations.RunSQL('INSERT INTO `softwarelibs` (`softwarelibName`, `softwarelibURL`) VALUES ("Thư viện Nhận diện hành vi bất thường", "ACTION_ABNORM_REG");'),
        migrations.RunSQL('INSERT INTO `softwarelibs` (`softwarelibName`, `softwarelibURL`) VALUES ("Thư viện Phát hiện khuôn mặt", "FACE_DETECT");')
    ]