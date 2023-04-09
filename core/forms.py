#csrf token 
from django import forms
from .models import ledger_category, ledger_fiscal_operations, ledger_operation_type, ledger_shop

class RecordForm(forms.ModelForm):
    operation_type = forms.ModelMultipleChoiceField(queryset = ledger_operation_type.objects.all())
    shop = forms.ModelMultipleChoiceField(queryset = ledger_shop.objects.all())

    class Meta:
        model = ledger_fiscal_operations
        fields = ["rrn","operation_type_id", "shop_id", "amt", "date"]