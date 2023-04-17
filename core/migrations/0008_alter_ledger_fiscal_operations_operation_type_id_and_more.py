# Generated by Django 4.1.7 on 2023-04-14 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_alter_fiscaloperationsalias_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="operation_type_id",
            field=models.ForeignKey(
                db_column="operation_type_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.ledger_operation_type",
            ),
        ),
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="shop_id",
            field=models.ForeignKey(
                db_column="shop_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.ledger_shop",
            ),
        ),
    ]