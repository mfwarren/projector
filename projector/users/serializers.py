from .models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'password'
        )
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        user = super(UserSerializer, self).restore_object(attrs, instance)

        password = attrs.get('password', None)

        if password:
            user.set_password(password)

        return user
