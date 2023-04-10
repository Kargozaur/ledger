# схема для core

from django.urls import path
from . import views
from .views import HomePageView, HistoryView, CreateFiscalOperation

app_name = "core"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("history/", HistoryView.as_view(), name="history"),
    path(
        "create_fiscal_operation/",
        CreateFiscalOperation.as_view(),
        name="create_fiscal_operation",
    ),
]
