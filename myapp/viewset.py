from rest_framework import viewsets
from .serializers import AdviserSerializers
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication

class AdviserViewset(viewsets.ModelViewSet):
    queryset = Adviser.objects.all()
    serializer_class = [AdviserSerializers]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
