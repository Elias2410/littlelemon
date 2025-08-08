from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Booking,Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# @permission_classes([IsAuthenticated])

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class CreateMenuItemsView(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
class BookingView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
class CreateBookingView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class SingleBookingView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]











# class bookingView(APIView):
#     def get(self,request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':'success','data':serializer.data})

# class menuView(APIView):

#     def get(self,request):
#         item = Menu.objects.all()
#         serializer = MenuSerializer(item, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':'success','data':serializer.data})
