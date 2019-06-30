# Generated by Django 2.1.4 on 2019-06-30 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('audit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Audit')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('rating', models.SmallIntegerField(default=0, null=True)),
            ],
            bases=('projects.audit',),
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('audit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Audit')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects')),
            ],
            bases=('projects.audit',),
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('audit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.Audit')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Steps')),
            ],
            bases=('projects.audit',),
        ),
    ]