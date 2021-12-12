from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import DatasetSerializer,DetailDatasetSerializer
from rest_framework.parsers import MultiPartParser,FileUploadParser
from rest_framework import status
from .models import Dataset

class Datasetview(APIView):
    parser_class = (FileUploadParser,MultiPartParser,)

    def post(self, request, format=None):
        serializer=DatasetSerializer(data=request.POST)
        file_obj = request.FILES['path']
        if serializer.is_valid():
            obj=Dataset.objects.create(
                name=serializer.validated_data['name'],
                user=serializer.validated_data['user'],
                path=file_obj
            )
            obj.save()

            return Response("Success")
        else:
            return Response('fail',status_code=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,):
        user = request.GET.get('user', None)
        id = request.GET.get('id', None)
        if (user):
            try:
                obj = Dataset.objects.get(user=user,id=id)
                obj.delete()
                return Response(
                    data={},
                    content_type="application/json",
                    status=status.HTTP_200_OK
                )
            except:
                pass
        return Response(
            data={},
            content_type="application/json",
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self,request):
        user=request.GET.get('user',None)
        if(user):
            obj=Dataset.objects.filter(user=user)
            deserializer=DetailDatasetSerializer(obj,many=True)
            return Response(
                data=deserializer.data,
            content_type="application/json",
                status = status.HTTP_200_OK
            )
        return Response(
            data={},
            content_type="application/json",
            status=status.HTTP_400_BAD_REQUEST
        )
