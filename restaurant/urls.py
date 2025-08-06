from django.urls import path,include
from .views import BookingView, CreateBookingView, SingleBookingView, MenuItemsView, SingleMenuItemView, CreateMenuItemsView, BookingViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables',BookingViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path('menu/', menuView.as_view(), name='menuView'),
    path('booking/', BookingView.as_view(), name='BookingView'),
    path('create_booking/', CreateBookingView.as_view(), name='CreateBookingView'),
    path('booking/<int:pk>', SingleBookingView.as_view(), name='SingleBookingView'),
    path('menu_item/', MenuItemsView.as_view(), name='MenuItemsView'),
    path('create_menu_item/', CreateMenuItemsView.as_view(), name='CreateMenuItemsView'),
    path('menu_item/<int:pk>', SingleMenuItemView.as_view(), name='SingleMenuItemView'),
    path('resturant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]