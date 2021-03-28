import os
import zipfile

from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status
from django.http import FileResponse, HttpResponse, JsonResponse
from rest_framework.response import Response

from .serializers import FolderSerializer, FolderFileSerializer, FileSerializer
from .models import Folder, File


class FolderView(views.APIView):
    """
    Getting information by current folder
    """
    def get(self, request, *args, **kwargs):
        folder_id = self.request.GET.get('id', None)
        if folder_id is not None:
            data = {'this_folder_data': Folder.objects.get(id=folder_id),
                    'folders': Folder.objects.filter(parent=folder_id),
                    'files': File.objects.filter(folder=folder_id)}
        else:
            data = {'this_folder_data': Folder.objects.get(id=1),
                    'folders': Folder.objects.filter(parent=1),
                    'files': File.objects.filter(folder=1)}
        serializer = FolderFileSerializer(data)
        return Response(serializer.data, status.HTTP_200_OK)


class UploadFileAPIView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = []


class CreateFolderAPIView(generics.CreateAPIView):
    """
    Created new folder in this current directory
    API example: 'localhost:8000/api/folders/create/?id=<id_current_folder>'
    """
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


def download_file(request, id):
    """
    Downloading clicked file
    """
    try:
        file = File.objects.get(pk=id)
        f = open(file.file.path, 'rb')
        response = FileResponse(f, as_attachment=True)
        return response
    except File.DoesNotExist:
        return JsonResponse({'Err':'File not found'}, status=404)


def download_folder_as_zip(request, id):
    """
    Download current folder as zip file.
    """
    try:
        folder_name = Folder.objects.get(pk=int(id)).name
        qs = File.objects.filter(folder=id)
        if qs.count() != 0:
            response = HttpResponse(content_type='application/zip')
            zip_file = zipfile.ZipFile(response, 'w')
            for f in qs:
                file_dir, file_name = os.path.split(f.file.path)
                zip_path = os.path.join(f'archive - {folder_name}', file_name)
                zip_file.write(f.file.path, zip_path)
            response['Content-Disposition'] = f'attachment; filename="{folder_name}"'
            return response
        else:
            return JsonResponse({'Err': 'Folder is empty'}, status=404)
    except Folder.DoesNotExist:
        return JsonResponse({'Err':'Does not exist'}, status=404)
