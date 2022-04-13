from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import APIView
from django.http.response import JsonResponse
from .models import Block, Building
from .serializers import BlockSerializer, BuildingSerializer



# connect to database
#connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+PASSWORD)

class BuildingList(generics.ListCreateAPIView):
    queryset = Building.objects.all();
    serializer_class = BuildingSerializer

class BuildingDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all();
    serializer_class = BuildingSerializer
    
class BlockList(generics.ListCreateAPIView):
    queryset = Block.objects.all();
    serializer_class = BlockSerializer

class BlockDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all();
    serializer_class = BlockSerializer
      
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
   
# # get all buildings
# @csrf_exempt
# @api_view(["GET"])
# def buildingList(request):
#     return JsonResponse(Building.objects.all(), safe=False)
    
#     d = {
#             "id": [],
#             "area": [],
#             "perimeter": [],
#             "kaek": [],
#             "numFloor": [],
#             "height": [],
#             "landUse": [],
#             "year": [],
#             "roof": []
#         }

#     query = f"SELECT id, area, perimeter, kaek, numFloor, height, landUse, year, roof from {TABLE}"
#     # fetch all relevant data from database
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query)
#         for row in cursor:
#             d["id"].append(row[0])
#             d["area"].append(row[1])
#             d["perimeter"].append(row[2])
#             d["kaek"].append(row[3])
#             d["numFloor"].append(row[4])
#             d["height"].append(row[5])
#             d["landUse"].append(row[6])
#             d["year"].append(row[7])
#             d["roof"].append(row[8])
#         cursor.close()
#     except Exception as e:
#         return JsonResponse({'message': str(e)}, status=500)
    
#     return Response(data = d)
    
# # get specific building
# @api_view(["GET"])
# def buildingDetail(request, id):
#     d = {}
    
#     # GET request (READ)
#     query = f"SELECT id, area, perimeter, kaek, numFloor, height, landUse, year, roof from {TABLE} WHERE id={id}"
#     # fetch all relevant data from database
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query)
#         for row in cursor:
#             print(row)
#             d["id"] = int(row[0])
#             d["area"] = row[1]
#             d["perimeter"] = row[2]
#             d["kaek"] = row[3]
#             d["numFloor"] = int(row[4])
#             d["height"] = row[5]
#             d["landUse"] = row[6]
#             d["year"] = row[7]
#             d["roof"] = row[8]
#         cursor.close()
#     except Exception as e:
#         return JsonResponse({'message': str(e)}, status = 500)
    
#     return JsonResponse(d, safe=False)
                
         
# @csrf_exempt
# @api_view(["POST"])
# def buildingCreate(request):
#     # POST request (CREATE)
#     query = f"""INSERT INTO {TABLE} (area, perimeter, kaek, numFloor, height, landUse, year, roof) VALUES
#             ({request.POST['area']}, {request.POST['perimeter']}, {request.POST['kaek']}, {request.POST['numFloor']},
#                 {request.POST['height']}, '{request.POST['landUse']}', {request.POST['year']}, '{request.POST['roof']}')""".replace("\n", "").replace("  ", "")
            
#     # insert data to table
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query)
#         connection.commit()
#         cursor.close()
#         return JsonResponse("Successfully added record into database", safe=False)
#     except Exception as e:
#         return JsonResponse({"message": str(e)}, status = 500)
        

# @csrf_exempt
# @api_view(["PUT"])
# def buildingUpdate(request, id):
#     # PUT request (UPDATE)
#     query = f"""UPDATE {TABLE} SET 
#                     area = {request.POST['area']}, perimeter = {request.POST['perimeter']}, kaek = {request.POST['kaek']},
#                     numFloor = {request.POST['numFloor']}, height = {request.POST['height']}, landUse = '{request.POST['landUse']}',
#                     year = {request.POST['year']}, roof = '{request.POST['roof']}'
#                 WHERE id = {id}""".replace("\n", "").replace("  ", "")
#     # update specific record
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query)
#         connection.commit()
#         cursor.close()
#     except Exception as e:
#         return JsonResponse({'message': str(e)}, status = 500)
    
#     return Response(f"Successfully updated building with id={id}")
        
        
# @csrf_exempt
# @api_view(["DELETE"])
# def buildingDelete(request, id):
#     # DELETE request     
#     query = f"DELETE FROM {TABLE} WHERE id={id}"
#     # delete specific record
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query)
#         connection.commit()
#         cursor.close()
#     except Exception as e:
#         print(e)
#         return JsonResponse({'message': str(e)}, status = 500)
    
#     return Response(f"Successfully deleted building with id={id}")
        