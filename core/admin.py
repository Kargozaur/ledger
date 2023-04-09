from django.contrib import admin
from .models import ledger_operation_type, ledger_fiscal_operations, ledger_shop, ledger_category

admin.site.register(ledger_operation_type)
admin.site.register(ledger_fiscal_operations)
admin.site.register(ledger_shop)
admin.site.register(ledger_category)