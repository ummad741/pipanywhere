from .models import UserMoney
from django.shortcuts import render
from .serializers import RegisterSerializer, AllMoneySerializer, User, AllMoney, ChiqimSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class UserRegisterView(APIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        username = request.data.get('user_name')
        password = request.data.get('user_password')
        user = User.objects.create(user_name=username, user_password=password)
        access = AccessToken.for_user(user)
        refresh = RefreshToken.for_user(user)
        user.save()
        return Response({
            "status": "User created",
            'access': str(access),
            'refresh': str(refresh),
        })


class GetObjects(APIView):
    serializer = RegisterSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        user = User.objects.all()
        serializer = RegisterSerializer(user, many=True)
        return Response(serializer.data)


class AddMoneyView(APIView):
    serializer_class = AllMoneySerializer
    queryset = AllMoney.objects.all()

    def post(self, request):
        user_n = int(request.data.get("user_n"))
        total_money = request.data.get('total_money')
        pul = UserMoney.objects.all().filter(card_holder=user_n)

        for i in pul:
            user_puli = i.money

        if user_puli >= int(total_money):
            qolgan_pul = user_puli - int(total_money)
            print(qolgan_pul)
            serializer = AllMoneySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print("Save")
            try:
                updater = UserMoney.objects.all().filter(
                    card_holder=user_n).update(money=qolgan_pul)
            except:
                return Response("Sizning Kartangiz yo'q")
            return Response({"MSG": "succses"})
        else:
            return Response({"MSG": "Sizning Pulingiz yetmaydi"})


class FilterMoney(APIView):
    serializer_class = ChiqimSerializer
    queryset = AllMoney.objects.all()

    def post(self, request):
        user_n = request.data.get("user_n")
        type_of_money = request.data.get("type_of_money")
        chiqim = AllMoney.objects.all().filter(
            user_n=user_n, type_of_money=type_of_money)
        money = 0
        for i in chiqim:
            money += i.total_money

        serializer = AllMoneySerializer(chiqim, many=True)
        return Response({"Data": serializer.data,
                         f"Barcha {type_of_money} lar": money
                         })


class Top3User(APIView):
    def get(self, request):
        users_list = []
        dict_kirim = {}
        dict_chiqim = {}
        data_user = User.objects.all()

        for i in data_user:
            users_list.append(i.id)

        for id in users_list:
            pul = AllMoney.objects.filter(
                user_n_id=id, type_of_money="Kirim").all()

        for id in users_list:
            pul = AllMoney.objects.filter(
                user_n_id=id, type_of_money="Chiqim").all()
            pul_odam = 0
            pul_odam += pul.total_money
            dict_kirim[id] = pul_odam
            print('chiqim ', dict_chiqim)

        asosiy_hisob_kitob = {}
        kirimlar = list(dict_kirim.values())
        chiqimlar = list(dict_chiqim.values())

        for t in range(len(kirimlar)):
            total_month = kirimlar[t] - chiqimlar[t]
            asosiy_hisob_kitob[t + 1] = total_month

        print(asosiy_hisob_kitob)

        sorted_asosiy_hisob_kitob = dict(
            sorted(asosiy_hisob_kitob.items(), key=lambda item: item[1], reverse=True))

        top3_users = dict(list(sorted_asosiy_hisob_kitob.items())[:3])

        return Response(top3_users)
