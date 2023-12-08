from django.urls import path
from .views import UserRegisterView, AddMoneyView, FilterMoney, Top3User, GetObjects
urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("GetObjects/", GetObjects.as_view()),
    path("money/", AddMoneyView.as_view()),
    path("chiqim/", FilterMoney.as_view()),
    path("top3/", Top3User.as_view()),
]
