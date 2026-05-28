
from rest_framework import serializers
from note.models import Note



class NoteSerializer(serializers.ModelSerializer):




    def validate(self, attrs):
        if True:
            res = super().validate(attrs=attrs)
            return res

    def to_representation(self, instance):
        response = super().to_representation(instance=instance)

        return response

    class Meta:
        model = Note
        fields = [ 'title', 'content', 'entered_time' ]

