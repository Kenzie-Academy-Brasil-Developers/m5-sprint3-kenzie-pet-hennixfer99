from rest_framework.views import APIView, Response, status
from animals.serializers import AnimalSerializer
from animals.models import Animal


class AnimalsView(APIView):

   def get(self, request):
    animals = Animal.objects.all()
    serializer = AnimalSerializer(data = animals, many = True)
    serializer.is_valid()

    return Response(serializer.data , status.HTTP_200_OK)

   def post(self, request):  
      serializer = AnimalSerializer(data = request.data)
      serializer.is_valid(raise_exception = True)
      serializer.save()

      return Response(serializer.data , status.HTTP_201_CREATED)

class AnimalsViewOne(APIView):

   def get(self, request, id=int):
      try:
            animal = Animal.objects.get(id=id)
      except Animal.DoesNotExist:
            return Response({'details': 'Content not found'}, status.HTTP_404_NOT_FOUND)

      serializer = AnimalSerializer(data = animal)
      serializer.is_valid()   

      return Response(serializer.data , status.HTTP_200_OK)


   def patch(self, request, id=int):
      try:
            animal = Animal.objects.get(id=id)
      except Animal.DoesNotExist:
            return Response({'details': 'Content not found'}, status.HTTP_404_NOT_FOUND)

      animal.name = request.data.get('name', animal.name)
      animal.age = request.data.get('age', animal.age)
      animal.weight = request.data.get('weight', animal.weight)

      if request.data.get('group') != None:
         return Response({'group': 'You can not update group'}, status.HTTP_422_UNPROCESSABLE_ENTITY)
      
      if request.data.get('traits') != None:
         return Response({'traits': 'You can not update traits'}, status.HTTP_422_UNPROCESSABLE_ENTITY)

      
 
      animal.save()

      serializer = AnimalSerializer(data = animal)
      serializer.is_valid()   

      return Response(serializer.data , status.HTTP_200_OK)


   def delete(self, request, id=int):
      try:
            animal = Animal.objects.get(id=id)
      except Animal.DoesNotExist:
            return Response({'details': 'Content not found'}, status.HTTP_404_NOT_FOUND)
      
      animal.delete()

      return Response({""}, status.HTTP_204_NO_CONTENT)
