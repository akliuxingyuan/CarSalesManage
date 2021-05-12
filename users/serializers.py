from rest_framework import serializers

from .models import User, Role, Right


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'rid',
            'username',
            'password',
            'mobile',
            'email'
        )

    def create(self, validated_data):
        """
        创建用户
        """
        user = super().create(validated_data)
        # 调用django的认证系统加密密码
        user.set_password(validated_data['password'])
        user.save()
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'id',
            'roleName',
            'roleDesc',
            'rights'
        )


class RightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = (
            'id',
            'authName',
            'authDesc'
        )
