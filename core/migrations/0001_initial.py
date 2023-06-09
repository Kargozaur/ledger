# Generated by Django 4.1.7 on 2023-03-31 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ledger_category",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_column="id",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(db_column="name", max_length=4000),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_at"
                    ),
                ),
            ],
            options={
                "db_table": "ledger_category",
            },
        ),
        migrations.CreateModel(
            name="ledger_operation_type",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_column="id",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(db_column="name", max_length=4000),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_at"
                    ),
                ),
            ],
            options={
                "db_table": "ledger_operation_type",
            },
        ),
        migrations.CreateModel(
            name="ledger_shop",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_column="id",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(db_column="name", max_length=4000),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_at"
                    ),
                ),
                (
                    "category_id",
                    models.ForeignKey(
                        db_column="category_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.ledger_category",
                    ),
                ),
            ],
            options={
                "db_table": "ledger_shop",
            },
        ),
        migrations.CreateModel(
            name="ledger_fiscal_operations",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        db_column="id",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("rrn", models.IntegerField(db_column="rrn")),
                (
                    "operation_type_id",
                    models.IntegerField(db_column="operation_type_id"),
                ),
                (
                    "date",
                    models.DateTimeField(auto_now_add=True, db_column="date"),
                ),
                (
                    "amt",
                    models.DecimalField(
                        db_column="amt", decimal_places=2, max_digits=8
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_at"
                    ),
                ),
                (
                    "shop_id",
                    models.ForeignKey(
                        db_column="shop_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.ledger_shop",
                    ),
                ),
            ],
            options={
                "db_table": "ledger_fiscal_operations",
            },
        ),
    ]
