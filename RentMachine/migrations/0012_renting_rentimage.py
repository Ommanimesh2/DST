# Generated by Django 4.1.7 on 2023-04-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentMachine', '0011_alter_orders_machine_id_alter_orders_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='renting',
            name='rentimage',
            field=models.CharField(default='https://firebasestorage.googleapis.com/v0/b/bhoomirent-df650.appspot.com/o/rn_image_picker_lib_temp_2512f23f-19ab-4ea7-9a4a-48ae50b9de9c.jpg?alt=media&token=7293eb19-9505-4910-8eb9-ee58d2f14ae5', max_length=1000),
        ),
    ]