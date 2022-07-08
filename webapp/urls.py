from django.urls import path
from .views import ChurnRateDetect

urlpatterns = [
    path('', ChurnRateDetect, name='churn_show'),
]