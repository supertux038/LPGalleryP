from rest_framework import serializers

from gallery.models import LPModel, User, Community


class LPModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = LPModel
        fields = '__all__'


