# Generated by Django 3.0.5 on 2020-04-04 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viciapp', '0006_auto_20200404_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='viciapp.Company'),
        ),
    ]
