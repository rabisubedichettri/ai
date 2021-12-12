
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import DataModelSerializer,DetailDataModelSerializer
from rest_framework.parsers import MultiPartParser,FileUploadParser
from rest_framework import status
from .models import DataModel

class Modelview(APIView):
    parser_class = (FileUploadParser,MultiPartParser,)

    #traning data set
    def post(self, request, format=None):
        serializer=DataModelSerializer(data=request.POST)
        file_obj = request.FILES['path']
        if serializer.is_valid():
            obj=DataModel.objects.create(
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
        if (user and id):
            try:
                obj = DataModel.objects.get(dataset__user=user,id=id)
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
            obj=DataModel.objects.filter(dataset__user=user)
            deserializer=DetailDataModelSerializer(obj,many=True)
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

