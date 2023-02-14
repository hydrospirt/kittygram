# from django.http import Http404
# from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from rest_framework import viewsets

from cats.models import Cat
from cats.serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer



# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatDetail(generics.RetrieveDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class APICat_Detail(APIView):
#     def get_object(self, pk):
#         try:
#             return Cat.objects.get(pk=pk)
#         except Cat.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         cat = self.get_object(pk)
#         serializer = CatSerializer(cat)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         cat = self.get_object(pk)
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         cat = self.get_object(pk)
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         cat = self.get_object(pk)
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def cat_detail(request, pk):
#     cat = Cat.objects.get(pk=pk)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = CatSerializer(cat)
#     return Response(serializer.data)

