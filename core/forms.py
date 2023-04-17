from django import forms
from .models import (
    ledger_category,
    ledger_fiscal_operations,
    ledger_operation_type,
    ledger_shop,
)


from django import forms
from .models import ledger_fiscal_operations, ledger_operation_type, ledger_shop

class RecordForm(forms.ModelForm):
    #drop-листы для выбора операции и магазина
    operation_type_id = forms.ModelChoiceField(
        queryset=ledger_operation_type.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-control"},
        ),
        #label="Operation Type",
    )
    shop_id = forms.ModelChoiceField(
        queryset=ledger_shop.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-control"},
        ),
        #label="Shop",
    )

    class Meta:
        model = ledger_fiscal_operations
        fields = [
            "rrn",
            "operation_type_id",
            "shop_id",
            "date",
            "amt",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control"}),
            "amt": forms.NumberInput(attrs={"class": "form-control"}),
        }

    # проверка rrn
    def clean_rrn(self):
        rrn = self.cleaned_data.get("rrn")
        if rrn and len(str(rrn)) != 12:
            raise forms.ValidationError("RRN должен состоять из 12 символов")
        else:
            rrn = self.instance.id if rrn is None or rrn == "" else rrn
        return rrn
    
    #доп настройки -> rrn не обязательное поле 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["rrn"].required = False
        self.fields["operation_type_id"].queryset = ledger_operation_type.objects.all()