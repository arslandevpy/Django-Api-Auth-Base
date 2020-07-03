# Generated by Django 3.0.6 on 2020-06-27 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200627_0541'),
        ('event_controller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmain',
            name='address_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_address', to='user.AddressGlobal'),
        ),
    ]