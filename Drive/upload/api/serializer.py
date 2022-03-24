from rest_framework import serializers
from upload.models import*

class UploadSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UploadDoc
        fields = '__all__'
        
class FolderSerializerDV(serializers.ModelSerializer):
    folder_file = Folder.folder_name
    folder_file= UploadSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    creater_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Folder
        fields='__all__'
        
class FolderSerializer(serializers.ModelSerializer):
    creater_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Folder
        fields='__all__'
        
        
