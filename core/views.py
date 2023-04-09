from django.shortcuts import render,redirect
from .forms import RecordForm
from .models import ledger_category, ledger_fiscal_operations, ledger_operation_type, ledger_shop
from django.http import HttpResponse
# Create your views here.

def index(request):
    operations = ledger_fiscal_operations.objects.order_by('-date')[:5]
    return render(request, 'core/index.html', {'operations':operations})


def history(request):
    fiscal_operations = ledger_fiscal_operations.objects.all().order_by('-created_at')
    return render(request, 'core/history.html', {'fiscal_operations': fiscal_operations})


def add_operation(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else: 
        form = RecordForm()
    return render(request, 'core/add_operation.html', {'form' : form})