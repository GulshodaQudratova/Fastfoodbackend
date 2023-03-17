from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router =  DefaultRouter()
router.register('botuser',BotUserViewSet)
router.register('category',CategoryViewSet)
router.register('subcategory',SubCategoryViewSet)
router.register('product',ProductViewSet)
router.register('order',OrderViewSet)
router.register('orderitem',OrderItemViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('change/',ChangeLanguage.as_view()),
    path('phone/',ChangePhoneNumber.as_view()),
    path('shop/',OrderedItems.as_view()),
    path('set_order/',SetOrderItem.as_view()),
    path('delete_basket/',DestroyBasket.as_view()),
    path('user/',BotUserInfo.as_view()),
    path('delete_item/',DeleteItem.as_view())
]