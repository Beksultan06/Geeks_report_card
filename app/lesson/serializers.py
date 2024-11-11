from rest_framework import serializers
from app.lesson.models import Lesson
from app.users.models import CustomUser

class LessonSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = Lesson
        fields = ["id", "direction", "type_lesson", "data", "end_data", "audience", "user"]

    def validate(self, attrs):
        user = attrs.get("user")
        data = attrs.get("data")
        end_data = attrs.get("end_data")
        audience = attrs.get("audience")
        request_user = self.context['request'].user

        # Проверка: убедитесь, что пользователь авторизован
        if request_user.is_anonymous:
            raise serializers.ValidationError("Пользователь не авторизован.")

        # Проверка: только менеджеры могут назначать уроки для других пользователей
        if request_user.role != "Менеджер" and user != request_user:
            raise serializers.ValidationError("Вы не можете назначить урок для другого пользователя.")

        # Проверка на наличие существующего урока для пользователя в то же время
        if Lesson.objects.filter(user=user, data=data).exists():
            raise serializers.ValidationError("У пользователя уже есть урок на это время.")

        # Проверка на занятость аудитории в указанное время
        if Lesson.objects.filter(audience=audience, data__lt=end_data, end_data__gt=data).exists():
            raise serializers.ValidationError("В это время в данной аудитории уже запланирован урок.")

        return attrs
