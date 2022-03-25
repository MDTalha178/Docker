from django.urls import path, include
# from apps.files import views as FileViews
from upload.api.views import *


urlpatterns = [
    path('', Allfolder.as_view(), name='folder'),
    path('<int:pk>', FolderDetail.as_view(), name='folder-detail'),
     path('<int:pk>/file', UploadFile.as_view(), name='uploadfile'),
    path('file<int:pk>', UpdateFile.as_view(), name='updatefile'),
]
