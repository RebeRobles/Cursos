# Generated by Django 3.2.6 on 2021-10-03 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='descrip_curse', to='curso_app.curse'),
        ),
    ]
