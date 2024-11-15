from rest_framework import serializers
from app.lesson.models import Lesson
from app.users.models import CustomUser

class LessonSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = Lesson
        fields = ["id", "direction", "type_lesson", "data", "audience", "user"]

    def validate(self, attrs):
        user = attrs.get("user")
        data = attrs.get("data")
        audience = attrs.get("audience")
        request_user = self.context['request'].user

        if request_user.is_anonymous:
            raise serializers.ValidationError("Пользователь не авторизован.")

        if request_user.role != "Менеджер" and user != request_user:
            raise serializers.ValidationError("Вы не можете назначить урок для другого пользователя.")

        if Lesson.objects.filter(user=user, data=data).exists():
            raise serializers.ValidationError("У пользователя уже есть урок на это время.")

        if Lesson.objects.filter(audience=audience, end_data__gt=data).exists():
            raise serializers.ValidationError("В это время в данной аудитории уже запланирован урок.")

        return attrs
