from django.contrib.auth.models import User, Group
from rest_framework import serializers

# The HyperlinkedModelSerializer class is similar to the ModelSerializer class except that it uses hyperlinks to represent relationships, rather than primary keys.
# The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields. The ModelSerializer class is the same as a regular Serializer class, except that: It will automatically generate a set of fields for you, based on the model.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']