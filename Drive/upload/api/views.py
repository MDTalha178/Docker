from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from upload.api.serializer import*
from  upload.models import UploadDoc
from upload.api.permisssion import*
from upload.models import*
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework import generics
from rest_framework import filters
from upload.api.pagination import FolderPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

class Allfolder(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    pagination_class = FolderPagination
    serializer_class = FolderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['folder_name']
    
    def get_queryse(self, request):
        queryset = self.get_queryset()
        serializer = FolderSerializer(queryset)
        return Response(serializer.data)
              
class FolderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializerDV
    
    
# Getting all the upload file (Get request)
class UploadFile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        files = UploadDoc.objects.all()
        serializer = UploadSerializer(files, many=True)
        return Response(serializer.data)
    
    def post(self,request,pk):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
       
class UpdateFile(APIView):
    permission_classes=[UploadUserOrReadOnly]    
    def put(self,request,pk):
        file = UploadDoc.objects.get(pk=pk)
        serializer = UploadSerializer(file,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
        
    
    def delete(self,request,pk):
        file = UploadDoc.objects.get(pk=pk)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)              

        

        
        