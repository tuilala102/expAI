# Generated by Django 4.1.3 on 2022-12-03 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('joined_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Joined at')),
                ('usrfullname', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='usrFullName', max_length=50, null=True)),
                ('usrdob', models.DateField(blank=True, db_column='usrDoB', null=True)),
                ('usrfaculty', models.CharField(blank=True, db_column='usrFaculty', max_length=45, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('classid', models.CharField(db_column='classID', max_length=20, primary_key=True, serialize=False)),
                ('classcode', models.CharField(blank=True, db_column='classCode', max_length=45, null=True)),
                ('classname', models.CharField(blank=True, db_column='className', max_length=45, null=True)),
                ('classschoolyear', models.CharField(blank=True, db_column='classSchoolYear', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Class',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Datasets',
            fields=[
                ('datasetid', models.CharField(db_column='datasetID', max_length=20, primary_key=True, serialize=False)),
                ('datasetname', models.CharField(blank=True, db_column='datasetName', max_length=100, null=True)),
                ('datasetfolderurl', models.CharField(blank=True, db_column='datasetFolderURL', max_length=200, null=True)),
                ('datasettraining', models.IntegerField(blank=True, db_column='datasetTraining', null=True)),
                ('datasettesting', models.IntegerField(blank=True, db_column='datasetTesting', null=True)),
                ('datasetsum', models.IntegerField(blank=True, db_column='datasetSum', null=True)),
                ('datasetcreator', models.CharField(blank=True, db_column='datasetCreator', max_length=20, null=True)),
                ('datasetcreatedtime', models.DateTimeField(blank=True, db_column='datasetCreatedTime', null=True)),
                ('datasetdescription', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='datasetDescription', max_length=200, null=True)),
                ('datasetowner', models.ForeignKey(blank=True, db_column='datasetOwner', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'datasets',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Evaluations',
            fields=[
                ('evaluateid', models.CharField(db_column='evaluateID', max_length=20, primary_key=True, serialize=False)),
                ('evaluateconfusionmatrixtraining', models.CharField(blank=True, db_column='evaluateConfusionMatrixTraining', max_length=45, null=True)),
                ('evaluateconfusionmatrixtesting', models.CharField(blank=True, db_column='evaluateConfusionMatrixTesting', max_length=45, null=True)),
                ('evaluateconfutionmatrixvalidation', models.CharField(blank=True, db_column='evaluateConfutionMatrixValidation', max_length=45, null=True)),
                ('evaluatenumclass', models.IntegerField(blank=True, db_column='evaluateNumClass', null=True)),
            ],
            options={
                'db_table': 'evaluations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Experiments',
            fields=[
                ('expid', models.CharField(db_column='expID', max_length=20, primary_key=True, serialize=False)),
                ('expname', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='expName', max_length=100, null=True)),
                ('exptype', models.CharField(blank=True, db_column='expType', max_length=10, null=True)),
                ('expcreatedtime', models.DateTimeField(blank=True, db_column='expCreatedTime', null=True)),
                ('expfilelog', models.CharField(blank=True, db_column='expFileLog', max_length=100, null=True)),
                ('expaftertrainmodelpath', models.CharField(blank=True, db_column='expAfterTrainModelPath', max_length=200, null=True)),
                ('expcreatorid', models.ForeignKey(blank=True, db_column='expCreatorID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('expdatasetid', models.ForeignKey(blank=True, db_column='expDatasetID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.datasets')),
            ],
            options={
                'db_table': 'experiments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('objid', models.CharField(db_column='objID', max_length=20, primary_key=True, serialize=False)),
                ('objname', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='objName', max_length=50, null=True)),
                ('objgeneralinfo', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='objGeneralInfo', max_length=500, null=True)),
                ('objurlfolder', models.CharField(blank=True, db_column='objURLFolder', max_length=200, null=True)),
                ('objcreatedtime', models.DateTimeField(blank=True, db_column='objCreatedTime', null=True)),
                ('objcreator', models.CharField(blank=True, db_column='objCreator', max_length=20, null=True)),
                ('objtype', models.CharField(blank=True, db_column='objType', max_length=45, null=True)),
            ],
            options={
                'db_table': 'objects',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Paramsconfigs',
            fields=[
                ('configid', models.IntegerField(db_column='configID', primary_key=True, serialize=False)),
                ('configimagesize', models.CharField(blank=True, db_column='configImageSize', max_length=45, null=True)),
                ('configlearningrate', models.FloatField(blank=True, db_column='configLearningRate', null=True)),
                ('configalgorithm', models.CharField(blank=True, db_column='configAlgorithm', max_length=45, null=True)),
                ('configepoch', models.IntegerField(blank=True, db_column='configEpoch', null=True)),
                ('configbatchsize', models.IntegerField(blank=True, db_column='configBatchSize', null=True)),
                ('configresid', models.CharField(blank=True, db_column='configResID', max_length=20, null=True)),
                ('configevaluateid', models.ForeignKey(blank=True, db_column='configEvaluateID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.evaluations')),
                ('configexpid', models.ForeignKey(blank=True, db_column='configExpID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.experiments')),
            ],
            options={
                'db_table': 'paramsconfigs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('roleid', models.IntegerField(db_column='roleID', primary_key=True, serialize=False)),
                ('rolename', models.CharField(blank=True, db_column='roleName', max_length=45, null=True, unique=True)),
            ],
            options={
                'db_table': 'roles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Softwarelibs',
            fields=[
                ('softwarelibid', models.CharField(db_column='softwarelibID', max_length=20, primary_key=True, serialize=False)),
                ('softwarelibname', models.CharField(blank=True, db_column='softwarelibName', max_length=45, null=True)),
                ('softwareliburl', models.CharField(blank=True, db_column='softwarelibURL', max_length=200, null=True)),
                ('softwarelibdescription', models.CharField(blank=True, db_column='softwarelibDescription', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'softwarelibs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TypePermission',
            fields=[
                ('typeid', models.AutoField(primary_key=True, serialize=False)),
                ('typename', models.CharField(blank=True, db_column='typeName', max_length=20, null=True)),
            ],
            options={
                'db_table': 'TypePermission',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('resultid', models.CharField(db_column='resultID', max_length=20, primary_key=True, serialize=False)),
                ('resulttestingdataset', models.CharField(blank=True, db_column='resultTestingDataset', max_length=20, null=True)),
                ('resultaccuracy', models.FloatField(blank=True, db_column='resultAccuracy', null=True)),
                ('resultdetail', models.CharField(blank=True, db_column='resultDetail', max_length=800, null=True)),
                ('resultconfigid', models.ForeignKey(blank=True, db_column='resultConfigID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.paramsconfigs')),
            ],
            options={
                'db_table': 'results',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('modelid', models.CharField(db_column='modelID', max_length=20, primary_key=True, serialize=False)),
                ('modelname', models.CharField(blank=True, db_column='modelName', max_length=100, null=True)),
                ('modeltype', models.CharField(blank=True, db_column='modelType', max_length=45, null=True)),
                ('modelfiletutorial', models.CharField(blank=True, db_column='modelFIleTutorial', max_length=200, null=True)),
                ('modelfiledescription', models.CharField(blank=True, db_column='modelFileDescription', max_length=200, null=True)),
                ('modeldescription', models.CharField(blank=True, db_column='modelDescription', max_length=45, null=True)),
                ('modeleventtype', models.CharField(blank=True, db_column='modelEventType', max_length=45, null=True)),
                ('modelcreator', models.CharField(blank=True, db_column='modelCreator', max_length=20, null=True)),
                ('modelcreatedtime', models.DateTimeField(blank=True, db_column='modelCreatedTime', null=True)),
                ('expsoftwarelibid', models.ForeignKey(blank=True, db_column='expSoftwareLibID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.softwarelibs')),
                ('modelowner', models.ForeignKey(blank=True, db_column='modelOwner', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'models',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='experiments',
            name='expmodelid',
            field=models.ForeignKey(blank=True, db_column='expModelID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.models'),
        ),
        migrations.AddField(
            model_name='experiments',
            name='expsoftwarelibid',
            field=models.ForeignKey(blank=True, db_column='expSoftwareLibID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.softwarelibs'),
        ),
        migrations.AddField(
            model_name='datasets',
            name='datasettype',
            field=models.ForeignKey(blank=True, db_column='datasetType', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.typepermission'),
        ),
        migrations.AddField(
            model_name='datasets',
            name='expsoftwarelibid',
            field=models.ForeignKey(blank=True, db_column='expSoftwareLibID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.softwarelibs'),
        ),
        migrations.AddField(
            model_name='user',
            name='roleid',
            field=models.ForeignKey(blank=True, db_column='roleid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.roles'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='usrclass',
            field=models.ManyToManyField(blank=True, db_column='usrclass', null=True, to='expAI.class'),
        ),
        migrations.CreateModel(
            name='Objectembeddings',
            fields=[
                ('objid', models.OneToOneField(db_column='objID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='expAI.objects')),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('expid', models.ForeignKey(db_column='expID', on_delete=django.db.models.deletion.DO_NOTHING, to='expAI.experiments')),
            ],
            options={
                'db_table': 'objectembeddings',
                'managed': True,
                'unique_together': {('objid', 'expid')},
            },
        ),
    ]
