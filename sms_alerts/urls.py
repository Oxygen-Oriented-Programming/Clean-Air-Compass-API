from django.urls import path
from .views import SmsAlertList, SmsAlertDetail

urlpatterns = [
    path("create/", SmsAlertList.as_view()),
    path("<int:pk>/", SmsAlertDetail.as_view()),
]
