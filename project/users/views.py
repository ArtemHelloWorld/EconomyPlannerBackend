from rest_framework import generics

from users.serializers import UserSerializer


class ProfileRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
