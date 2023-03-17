from django.shortcuts import render
#############################################################
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
###########################################################################
from .serializer import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters
class BotUserViewSet(ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['name']
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['name']
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['name']
class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['name']
class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class ChangeLanguage(APIView):
    def post(self,request):
        data = request.POST
        data = data.dict()
        telegram_id = data['telegram_id']
        user = BotUser.objects.get(telegram_id=telegram_id)
        user.language = data['language']
        user.save()
        return Response({'status':'Language changed.'})
class ChangePhoneNumber(APIView):
    def post(self,request):
        data = request.POST
        data = data.dict()
        telegram_id = data['telegram_id']
        user = BotUser.objects.get(telegram_id=telegram_id)
        user.phone = data['phone']
        user.save()
        return Response({'status':'Phone Number changed.'})
class OrderedItems(APIView):
    def post(self,request):
        data = request.POST
        data = data.dict()
        user = BotUser.objects.get(telegram_id=data['telegram_id'])
        orders = BotUser.objects.filter(user=user)
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)
class SetOrderItem(APIView):
    def post(self,request):
        data = request.POST
        data = data.dict()
        telegram_id = data['telegram_id']
        product = data['product']
        quantity = data['quantity']
        user = BotUser.objects.get(telegram_id=telegram_id)
        product = Product.objects.get(id=product)
        order,created = Order.objects.get_or_create(user=user)
        orderitem,created = OrderItem.objects.get_or_create(order=order,product=product)
        if int(quantity) == 0:
            orderitem.delete()
            return Response({'status':'Order Item Deleted.'})
        else:
            orderitem.quantity = quantity
            orderitem.save()
            return Response({'status':'Order Item Updated.'})
class DestroyBasket(APIView):
    def post(self,request):
        data = request.POST
        data = data.dict()
        telegram_id = data['telegram_id']
        user = BotUser.objects.get(telegram_id=telegram_id)
        try:
            order = Order.objects.get(user=user)
            order.delete()
        except Order.DoesNotExist:
            pass
        except Exception as e:
            pass
        return Response({'status':'Basket Deleted.'})
class BotUserInfo(APIView):
    def post(self,request):
        data = request.data 
        user = BotUser.objects.get(telegram_id=data['telegram_id'])
        serializer = BotUserSerializer(instance=user,partial=True)
        return Response(serializer.data)
class DeleteItem(APIView):
    def post(self,request):
        data = request.POST
        data = data.dict()
        telegram_id = data['telegram_id']
        product = data['product']
        user = BotUser.objects.get(telegram_id=telegram_id)
        product = Product.objects.get(id=product)
        order,created = Order.objects.get_or_create(user=user)
        orderitem,created = OrderItem.objects.get_or_create(order=order,product=product)
        orderitem.delete()
        return Response({'status':'Order Item Deleted.'})