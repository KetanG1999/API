from rest_framework import serializers
from .models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','firstname','lastname','city','age']
        read_only_fields = ['id']

        #add custom validator
        def validate(self,data):
            if(len(data['firstname'])) == 0:
                raise serializers.ValidationError({'error':'name should not be blank'})
            return data