# Generated by Django 4.1.7 on 2023-04-01 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_number', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='staffs/profiles')),
                ('staff_number', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('bio', models.CharField(blank=True, max_length=500, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=10)),
                ('dob', models.DateField(blank=True, null=True)),
                ('doj', models.DateField(blank=True, null=True)),
                ('working_hours', models.PositiveIntegerField(blank=True, default=10, null=True)),
                ('education', models.CharField(choices=[('High School', 'High School'), ('Diploma', 'Diploma'), ('Degree', 'Degree'), ('Masters', 'Masters'), ('PHD', 'Phd'), ('Doctrate', 'Doctrate')], default='Diploma', max_length=20)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('On Hold', 'On Hold'), ('Resigned', 'Resigned'), ('Terminated', 'Terminated'), ('Absconded', 'Absconded')], default='Active', max_length=20)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='office.department')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='office.employeegrade')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='office.staffposition')),
                ('shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='office.staffshift')),
                ('timetable', models.ManyToManyField(blank=True, to='office.timetable')),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staffs',
                'ordering': ['first_name', 'doj', 'staff_number'],
            },
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_head', to='staff.staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffNextBirthday',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('staff.staff',),
        ),
    ]
