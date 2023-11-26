from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.response import Response

from users.serializers import UserSerializer
from users.tasks import send_email


class UserCreationApiView(viewsets.GenericViewSet):
    serializer_class = UserSerializer

    # POST request handler
    def create(self, request):
        # Create a new user
        serializer = UserSerializer(data=request.data)

        # Validate the data
        serializer.is_valid(raise_exception=True)

        # Save the user
        serializer.save()
        
        # Send an email to the user
        send_email.delay(serializer.data['email'],
                         serializer.data['username'])

        # Return the user data
        return Response(serializer.data)
