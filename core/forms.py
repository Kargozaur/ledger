from django import forms
from .models import (
    ledger_category,
    ledger_fiscal_operations,
    ledger_operation_type,
    ledger_shop,
)


class RecordForm(forms.ModelForm):
    operation_type = forms.ModelChoiceField(
        queryset=ledger_operation_type.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    shop = forms.ModelChoiceField(
        queryset=ledger_shop.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = ledger_fiscal_operations
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control"}),
            "amt": forms.NumberInput(attrs={"class": "form-control"}),
        }

#проверка rrn 
    def clear_rrn(self): 
        rrn = self.cleaned_data.get("rrn")
        if len(str(rrn)) != 12 or len(str(rrn))!= 0:
            raise forms.ValidationError(
                "RRN должен состоять из 12 символов или пустой строкой"
            )
        return rrn
