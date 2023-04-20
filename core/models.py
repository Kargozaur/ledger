from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


# Models
class ledger_operation_type(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    name = models.TextField(db_column="name")
    created_at = models.DateField(db_column="created_at")

    class Meta:
        db_table = "ledger_operation_type"

    def __str__(self):
        return self.name


class ledger_category(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    name = models.TextField(db_column="name")
    created_at = models.DateField(db_column="created_at")

    class Meta:
        db_table = "ledger_category"

    def __str__(self):
        return self.name    


class ledger_shop(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    name = models.TextField(db_column="name")
    created_at = models.DateField(db_column="created_at")
    category_id = models.ForeignKey(
        ledger_category,
        to_field="id",
        on_delete=models.CASCADE,
        db_column="category_id",
    )

    class Meta:
        db_table = "ledger_shop"

    def __str__(self):
        return self.name


class ledger_fiscal_operations(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    rrn = models.BigIntegerField(unique=True, db_column="rrn", null=True, blank=True)
    operation_type_id = models.ForeignKey(
        ledger_operation_type,
        to_field="id",
        on_delete=models.CASCADE,
        db_column="operation_type_id",
    )
    shop_id = models.ForeignKey(
        ledger_shop,
        to_field="id",
        on_delete=models.CASCADE,
        db_column="shop_id",
    )
    date = models.DateField(db_column="date")
    amt = models.DecimalField(max_digits=8, decimal_places=2, db_column="amt")
    created_at = models.DateField(auto_now=True, db_column="created_at")

    class Meta:
        db_table = "ledger_fiscal_operations"

    def clean(self):
        if self.rrn and len(str(self.rrn)) != 12:
            raise ValidationError("RRN должен состоять из 12 символов")

    @transaction.atomic()
    def save_with_transaction(self, *args, **kwargs):
        if not self.rrn:
            self.save() # сохраняем объект, чтобы получить автоматически присвоенное значение id
            self.rrn = self.id
            super(ledger_fiscal_operations, self).save(*args, **kwargs)
        else:
            super(ledger_fiscal_operations, self).save(*args, **kwargs)
        
    
    #def clean(self):
    #    if self.rrn and len(str(self.rrn)) != 12:
    #        raise ValidationError("RRN должен состоять из 12 символов")

    #@transaction.atomic()
    #def save_with_transaction(self, *args, **kwargs):
    #    self.save(*args, **kwargs)


# Alias


#class ShopAlias(ledger_shop):
#    class Meta:
#        proxy = True
#        verbose_name = "Shop Alias"
#        verbose_name_plural = "Shops Alias"


# class FiscalOperationsAlias(ledger_fiscal_operations):
#    class Meta:
#        proxy = True
#        verbose_name = "Операция"
#        verbose_name_plural = "Операции"
#
#    @classmethod
#    @transaction.atomic
#    def create_operation(
#        cls, rrn, operation_type_name, shop_name, date, amt, created_at
#    ):
#        operation_type_alias = ledger_operation_type._meta.db_table
#        shop_alias = ShopAlias._meta.db_table
#        fiscal_operations_alias = FiscalOperationsAlias._meta.db_table
#
#        operation_type = ledger_operation_type.objects.get(
#            name=operation_type_name
#        )
#        shop = ShopAlias.objects.get(name=shop_name)
#        # получить id в переменную -> запихнуть в rrn
#        # id = cls.objects.raw(
#        #    f"SELECT setval(pg_get_serial_sequence('{fiscal_operations_alias}', 'id'), (SELECT MAX(id) FROM {fiscal_operations_alias}))"
#        # )
#        ledger_fiscal_operations.objects.create(
#            id=id,
#            rrn=rrn,
#            operation_type_id=operation_type.id,
#            shop_id=shop.id,
#            date=date,
#            amt=amt,
#            created_at=created_at,
#        )
#        cls.objects.raw(
#            f"SELECT setval(pg_get_serial_sequence('{fiscal_operations_alias}', 'id'), (SELECT MAX(id) FROM {fiscal_operations_alias}))"
#        )
#
