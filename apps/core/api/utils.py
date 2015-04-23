from rest_framework import serializers


class ObjectSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return obj.get_serialize_object()
