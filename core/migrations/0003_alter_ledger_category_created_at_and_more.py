# Generated by Django 4.1.7 on 2023-04-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_fiscaloperationsalias_shopalias_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ledger_category",
            name="created_at",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="ledger_category",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="ledger_category",
            name="name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="amt",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="created_at",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="rrn",
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name="ledger_fiscal_operations",
            name="shop_id",
            field=models.IntegerField(db_column="shop_id"),
        ),
        migrations.AlterField(
            model_name="ledger_operation_type",
            name="created_at",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="ledger_operation_type",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="ledger_operation_type",
            name="name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="ledger_shop",
            name="category_id",
            field=models.IntegerField(db_column="category_id"),
        ),
        migrations.AlterField(
            model_name="ledger_shop",
            name="created_at",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="ledger_shop",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="ledger_shop",
            name="name",
            field=models.TextField(),
        ),
        migrations.AlterModelTable(
            name="ledger_category",
            table="category",
        ),
        migrations.AlterModelTable(
            name="ledger_fiscal_operations",
            table=None,
        ),
        migrations.AlterModelTable(
            name="ledger_shop",
            table="shop",
        ),
    ]