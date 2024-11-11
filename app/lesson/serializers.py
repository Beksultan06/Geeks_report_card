from rest_framework import serializers
from app.lesson.models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Lesson
        fields = ["id", "direction", "type_lesson", "data", "audience", "user"]

    def validate(self, attrs):
        user = self.context['request'].user
        data = attrs.get("data")
        audience = attrs.get("audience")

        # Проверяем, есть ли у пользователя уже урок на это же время
        if Lesson.objects.filter(user=user, data=data).exists():
            raise serializers.ValidationError("У вас уже есть урок на это время.")
        # Проверяем, есть ли уже урок с той же аудиторией и временем
        if Lesson.objects.filter(audience=audience, data=data).exists():
            raise serializers.ValidationError("В это время в данной аудитории уже запланирован урок.")


        return attrs
