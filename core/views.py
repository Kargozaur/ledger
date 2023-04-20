from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .forms import RecordForm
from .models import ledger_fiscal_operations
from django.db import transaction
from django.http import HttpResponse


class HomePageView(ListView):
    model = ledger_fiscal_operations
    template_name = "home.html"
    context_object_name = "latest_operations"
    ordering = ["-created_at"]
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        for operation in queryset:
            operation_type_name = (
                operation.operation_type_id.name
            )  # Получение названия из связанной модели
            shop_name = (
                operation.shop_id.name
            )  # Получение названия из связанной модели
            operation.operation_type_name = operation_type_name
            operation.shop_name = shop_name
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object_list.exists():
            latest_operation = self.object_list[0]
            context["operation_type_name"] = latest_operation.operation_type_id.name
            context["shop_name"] = latest_operation.shop_id.name
        else:
            context["operation_type_name"] = None
            context["shop_name"] = None
        return context

class HistoryView(ListView):
    model = ledger_fiscal_operations
    template_name = "history.html"
    context_object_name = "all_operations"
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        for operation in queryset:
            operation_type_name = (
                operation.operation_type_id.name
            )  # Получение названия из связанной модели
            shop_name = (
                operation.shop_id.name
            )  # Получение названия из связанной модели
            operation.operation_type_name = operation_type_name
            operation.shop_name = shop_name
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object_list.exists():
            context["operation_type_name"] = self.object_list[0].operation_type_id.name
            context["shop_name"] = self.object_list[0].shop_id.name
        else:
            context["operation_type_name"] = None
            context["shop_name"] = None
        return context


class CreateFiscalOperation(CreateView):
    model = ledger_fiscal_operations
    form_class = RecordForm
    template_name = "create_fiscal_operation.html"
    success_url = reverse_lazy("create_fiscal_operation")

    def form_valid(self, form):
        try:
            # Получаем данные из формы
            form.instance.rrn = form.cleaned_data.get("rrn")
            form.instance.operation_type_id = form.cleaned_data.get("operation_type_id")
            form.instance.shop_id = form.cleaned_data.get("shop_id")
            form.instance.date = form.cleaned_data.get("date")
            form.instance.amt = form.cleaned_data.get("amt")
            form.instance.created_at = form.cleaned_data.get("created_at")
            if not form.instance.rrn:
                form.instance.rrn = form.instance.id  # Присваиваем значение id полю rrn
            form.save()  # Сохраняем объект модели в БД

            # Выводим сообщение об успешном создании объекта
            messages.success(self.request, "Операция создана успешно")
            return super().form_valid(form)
        except Exception as e:
            # В случае возникновения ошибки выводим сообщение об ошибке
            messages.error(
                self.request, f"Случилась ошибка при создании операции: {e}"
            )
            return super().form_invalid(form)

    def get_success_url(self):
        return self.request.path
