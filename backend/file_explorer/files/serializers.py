from rest_framework import serializers
from .models import Folder, File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'folder', 'name', 'file', 'upload_date')


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ('id', 'parent', 'name', 'created_on')


class FolderFileSerializer(serializers.Serializer):
    this_folder_data = FolderSerializer(read_only=True)
    folders = FolderSerializer(read_only=True, many=True)
    files = FileSerializer(read_only=True, many=True)
