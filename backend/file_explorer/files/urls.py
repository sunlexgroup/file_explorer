from django.urls import path
from .views import UploadFileAPIView, CreateFolderAPIView, download_file, download_folder_as_zip, FolderView


urlpatterns = [
    path('files/download/<id>', download_file), # скачивание файла
    path('files/upload/', UploadFileAPIView.as_view()), # загрузка файла
    path('folders/', FolderView.as_view()), # показывает папки текущей директории
    path('folders/create/', CreateFolderAPIView.as_view()),  # создает дочернюю директорию в текущей папке
    path('folders/download/<id>', download_folder_as_zip) # скачивание папки в виде архива zip
]