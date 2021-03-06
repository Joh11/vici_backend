# Generated by Django 3.0.5 on 2020-04-04 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viciapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='adress',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='opening_hours',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='viciapp.Company')),
            ],
        ),
    ]
