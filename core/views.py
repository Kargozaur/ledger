from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .forms import RecordForm
from django.utils import timezone
from .models import (
    ledger_category,
    ledger_fiscal_operations,
    ledger_operation_type,
    ledger_shop,
    FiscalOperationsAlias,
)
import datetime

# Create your views here.

# def HomePageView(request):
#    operations = ledger_fiscal_operations.objects.order_by('-date')[:5]
#    return render(request, 'core/index.html', {'operations':operations})


class HomePageView(ListView):
    model = ledger_fiscal_operations
    template_name = "home.html"
    context_object_name = "latest_operations"
    ordering = ["-created_at"]
    paginate_by = 5


class HistoryView(ListView):
    model = ledger_fiscal_operations
    template_name = "history.html"
    context_object_name = "all_operations"
    ordering = ["-created_at"]


# def HistoryView(request):
#    fiscal_operations = ledger_fiscal_operations.objects.all().order_by('-created_at')
#    return render(request, 'core/history.html', {'fiscal_operations': fiscal_operations})


class CreateFiscalOperation(CreateView):
    model = ledger_fiscal_operations
    form_class = RecordForm
    template_name = "create_fiscal_operation.html"

    # Определение метода получения URL (redirect)
    def get_success_url(self):
        return reverse("create_fiscal_operation")

    def form_valid(self, form):
        try:
            rrn = form.cleaned_data.get("rrn")
            if len(str(rrn)) != 12 or len(str(rrn))!= 0:
                messages.error(
                    self.request, "RRN должен состоять из 12 символов или пустой строкой"
                )
                return self.form_invalid(form)

            operation_type_name = form.cleaned_data.get(
                "operation_type"
            )
            shop_name = form.cleaned_data.get("shop")
            date = form.cleaned_data.get("date")
            amt = form.cleaned_data.get("amt")
            created_at = datetime.datetime.now()

            FiscalOperationsAlias.create_operation(
                rrn,
                operation_type_name,
                shop_name,
                date,
                amt,
                created_at,
            )

            messages.success(self.request, "Операция создана успешно")
        except Exception as e:
            messages.error(
                self.request,
                f"Случилась ошибка при создании операции {e}",
            )
        return super().form_valid(form)

    # метод для обработки валидной формы
    # def form_valid(self, form):
    #    try:
    #        rrn = form.cleaned_data.get('rrn')
    #        if len(rrn) != 12:
    #            messages.error(self.request, 'RRN должен состоять из 12 символов')
    #            return self.form_invalid(form)
    #
    #        self.object = form.save()
    #        messages.success(self.request, 'Операция создана успешно')
    #    except Exception as e:
    #        messages.error(self.request, f'Случилась ошибка при создании операции {e}')
    #    return super().form_valid(form)

    # class CreateFiscalOperation(View):


#    def get(self, request):
#        form = FiscalOperationsAlias
#        return render(request, 'create_fiscal_operation.html', {'form':form})
#
#    def post(self, request):
#        form = RecordForm(request.POST)
#        if form.is_valid():
#            rrn = form.cleaned_data['rrn']
#            operation_type = form.cleaned_data['operation_type'].name
#            shop = form.cleaned_data['shop'].name
#            date = form.cleaned_data['date']
#            amt = form.cleaned_data['amt']
#            created_at = form.cleaned_data['created_at']
#
#            try:
#                FiscalOperationsAlias.create_operation(rrn, operation_type, shop, date, amt,created_at)
#                messages.success(request, 'Операция создана успешно')
#            except Exception as e:
#                messages.error(request, f'Случилась ошибка при создании операции {e}')
#            return redirect('create_fiscal_operation')
#        return render(request, 'core:create_fiscal_operation.html', {'form':form})

# class CreateFiscalOperation(CreateView):
#    model = ledger_fiscal_operations
#    form_class = RecordForm
#    template_name = 'create_fiscal_operation.html'
#    success_url = reverse_lazy('create_fiscal_operation')
#
#    def form_valid(self, form):
#        try:
#            form.save()
#            messages.success(self.request, 'Операция создана успешно')
#        except Exception as e:
#            messages.error(self.request, f'Случилась ошибка при создании операции {e}')
#        return super().form_valid(form)
#
#    def form_invalid(self, form):
#        messages.error(self.request, 'Ошибка при заполнении формы')
#        return super().form_invalid(form)
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['form'] = self.form_class()
#        return context
