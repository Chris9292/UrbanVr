from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Block, Building
from .serializers import BlockSerializer, BuildingSerializer


class BuildingList(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    
class BlockList(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

class BlockDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    
    
@api_view(['PATCH'])
def buildingUpdatePartial(request, pk):
    
    try: 
        building = Building.objects.get(pk=pk)
    except Building.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # check which fields to update based on request dataclass
    
    fields_to_update = []
    
    if "kaek" in request.data:
        fields_to_update.append("kaek")
        building.kaek = request.data.get("kaek")
        
    # to fix: not updating this field
    if "perimeter" in request.data:
        fields_to_update.append("perimeter")
        building.perimeter = request.data.get("perimeter")
        
    if "area" in request.data:
        fields_to_update.append("area")
        building.area = request.data.get("area")
    
    if "numfloor" in request.data:
        fields_to_update.append("numfloor")
        building.numfloor = request.data.get("numfloor")
        
    if "height" in request.data:
        fields_to_update.append("height")
        building.height = request.data.get("height")

    if "year" in request.data:
        fields_to_update.append("year")
        building.year = request.data.get("year")
        
    # to fix: not updating this field
    if "landuse" in request.data:
        fields_to_update.append("landuse")
        building.landuse = request.data.get("landuse")
        
    if "roof" in request.data:
        fields_to_update.append("roof")
        building.roof = request.data.get("roof")
    
    # save requested fields
    try:
        building.save(update_fields = fields_to_update)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=e)
    
    return Response(status=status.HTTP_200_OK, data=BuildingSerializer(building).data)

    
@api_view(["GET"])
def apiOverview(request):
    return Response(
        {
            "Block":
                {
                    "List": "/blocks/",
                    "Detail": "/block/<int:id>/" 
                },
            "Building":
                {
                    "List": "/buildings/",
                    "Detail": "/building/<int:id>/"
                }
        }
    )
    