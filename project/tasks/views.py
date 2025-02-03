from django.db.models import Q, F

from tasks.models import Task
from users.models import User
from tasks.serializers import TaskSerializer
from rest_framework import generics


class TasksList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(users__in=[user])
    
    def perform_create(self, serializer):
        users = serializer.validated_data.get('users', [])
        users.append(self.request.user)
        users.append(User.objects.get(pk=4))
        serializer.save(users=users)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'task_pk'


class TaskStatisticList(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        subordinates = user.subordinates.all()
        print(subordinates)
        return Task.objects.filter(status=True).filter(Q(users__in=[user]) | Q(users__in=subordinates)).distinct()
