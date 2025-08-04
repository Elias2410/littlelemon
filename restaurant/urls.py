from django.urls import path,include
from . import views
from .views import menuView, bookingView, MenuItemsView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables',BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', menuView.as_view(), name='menuView'),
    path('booking/', bookingView.as_view(), name='bookingView'),
    path('menu_item/', MenuItemsView.as_view(), name='MenuItemsView'),
    path('menu_item/<int:pk>', SingleMenuItemView.as_view(), name='SingleMenuItemView'),
    path('resturant/booking/', include(router.urls))
]