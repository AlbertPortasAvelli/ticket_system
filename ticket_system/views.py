from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class CustomTokenObtainPairView(TokenObtainPairView):
    
    def post(selfl, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            "access": response.data["access"],
            "refresh": response.data["refresh"],
            "message": "Successful Login"
        })
    
class LogoutView(APIView):
    
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            
        
            refresh_token = request.data.get('refresh')

            if not refresh_token:
                return Response({"error": "No refresh token provided"}, status=status.HTTP_400_BAD_REQUEST)

            
            token = RefreshToken(refresh_token)
            
            
            token.blacklist()

            return Response({"message": "Successful Logout"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Could not Log out: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)