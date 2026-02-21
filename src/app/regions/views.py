from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema
from .models import Region
from .serializers import RegionSerializer


@extend_schema(
    tags=['Regions'],
    summary='List or create regions',
    description='GET: Returns all Tanzania regions. POST: Create a new region (authenticated users only).',
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def region_list_create(request):
    if request.method == 'GET':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)
    serializer = RegionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Regions'],
    summary='Retrieve, update or delete a region',
    description='GET: Retrieve a region by slug. PUT/PATCH: Update it. DELETE: Remove it (authenticated users only).',
)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def region_detail(request, slug):
    try:
        region = Region.objects.get(slug=slug)
    except Region.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = RegionSerializer(region, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
