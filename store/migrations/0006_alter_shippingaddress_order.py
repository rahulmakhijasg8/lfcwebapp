# Generated by Django 3.2.9 on 2021-11-15 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_is_boolean_product_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order'),
        ),
    ]
