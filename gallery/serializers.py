from rest_framework import serializers

from gallery.models import LPModel, Community, Comment, MainPage


class LPModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = LPModel
        fields = '__all__'


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class MainPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'

