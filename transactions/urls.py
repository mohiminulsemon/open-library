from django.urls import path
from .views import DepositMoneyView, TransactionReportView

# app_name = 'transactions'

urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
     path("report/", TransactionReportView.as_view(), name="transaction_report"),
]