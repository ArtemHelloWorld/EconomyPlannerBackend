from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from tasks.models import Task
from users.serializers import ProfileSerializer


class TaskSerializer(serializers.ModelSerializer):
    users = ProfileSerializer(many=True, read_only=True)
    time_completed = SerializerMethodField(allow_null=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'status',
            'users',
            'deadline_start',
            'deadline_end',
            'time_completed'
        )
        read_only_fields = ('id', 'time_completed')

    def validate_users(self, value):
        user_subordinates = self.context['request'].user.subordinates.all()
        for user in value:
            if user not in user_subordinates:
                raise serializers.ValidationError(
                    f'Вы не можете назначить задачу {user.username} '
                    f'так как он не ваш подчиненный'
                )
        return value

    def get_time_completed(self, obj):
        print(obj.date_completed)
        if obj.date_completed:
            timedelta_value = obj.date_completed - obj.date_created
            days = timedelta_value.days
            hours, remainder = divmod(timedelta_value.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            readable_duration = ""
            if days:
                readable_duration += f"{days} дней "
            if hours:
                readable_duration += f"{hours} часов "
            readable_duration += f"{minutes} минут"
            return readable_duration
        return None

