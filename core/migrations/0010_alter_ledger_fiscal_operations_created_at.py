# Generated by Django 4.1.7 on 2023-04-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_alter_ledger_fiscal_operations_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="created_at",
            field=models.DateField(auto_now=True, db_column="created_at"),
        ),
    ]
