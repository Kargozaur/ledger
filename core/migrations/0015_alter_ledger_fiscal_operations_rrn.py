# Generated by Django 4.1.7 on 2023-04-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0014_alter_ledger_fiscal_operations_rrn"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="rrn",
            field=models.BigIntegerField(
                blank=True,
                db_column="rrn",
                default=models.AutoField(
                    db_column="id", primary_key=True, serialize=False
                ),
                unique=True,
            ),
        ),
    ]
