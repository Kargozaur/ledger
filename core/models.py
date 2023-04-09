from django.db import models
from django.utils import timezone

#Models
class ledger_operation_type(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    name = models.CharField(max_length=4000, db_column='name')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')

    class Meta:
        db_table = "ledger_operation_type"
    
    def __str__(self):
        return self.name
    
class ledger_category(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=4000, db_column='name')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    
    class Meta:
        db_table = "ledger_category"
    
    def __str__(self):
        return self.name

class ledger_shop(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=4000, db_column='name')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    category_id = models.ForeignKey(ledger_category, on_delete=models.CASCADE, to_field='id' ,db_column='category_id')

    class Meta:
        db_table = "ledger_shop"

    def __str__(self):
        return self.name
    

class ledger_fiscal_operations(models.Model):
    id = models.AutoField(primary_key=True ,db_column='id') 
    rrn = models.IntegerField(db_column='rrn', unique=True)
    operation_type_id = models.IntegerField(db_column='operation_type_id')
    shop_id = models.ForeignKey(ledger_shop, to_field='id', db_column='shop_id' ,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, db_column='date')
    amt = models.DecimalField(max_digits=8, decimal_places=2, db_column='amt')
    created_at = models.DateTimeField(default=timezone.now, db_column='created_at')

    class Meta:
        db_table = "ledger_fiscal_operations"

    def __str__(self):
        return str(self.rrn)
    
#Alias
class OT(ledger_operation_type):
    class Meta:
        proxy = True
    
    def __str__(self):
        return self.name
    
class C(ledger_category):
    class Meta:
        proxy = True

    def __str__(self):
        return self.name
    
class S(ledger_shop):
    class Meta:
        proxy = True

    def __str__(self):
        return self.name
    
class FO(ledger_fiscal_operations):
    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.rrn}: {self.operation_type_id} - {self.shop_id} - {self.amt}'