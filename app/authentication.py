from .models import User
from django.contrib.auth.backends import BaseBackend


class EmailAuth(BaseBackend):
    def authenticate(self, request, email, password):
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None