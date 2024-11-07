from rest_framework.permissions import BasePermission

class IsManagerOrReadOnly(BasePermission):
    """
    Разрешает доступ к изменению данных только для пользователей с ролью 'Менеджер'.
    Пользователи с ролью 'Преподаватель' могут только просматривать данные.
    """
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return request.user.is_authenticated and request.user.role == "Менеджер"
