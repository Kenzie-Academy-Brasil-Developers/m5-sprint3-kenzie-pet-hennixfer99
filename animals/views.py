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

   def get(self, request, animal_id: int):
      try:
            animal = Animal.objects.get(id=animal_id) 
      except Animal.DoesNotExist:
            return Response({'details': 'Content not found'}, status.HTTP_404_NOT_FOUND)

      serializer = AnimalSerializer(animal)
      

      return Response(serializer.data , status.HTTP_200_OK)


   def patch(self, request, animal_id: int):
      try:
            animal = Animal.objects.get(id=animal_id)
      except Animal.DoesNotExist:
            return Response({'details': 'Content not found'}, status.HTTP_404_NOT_FOUND)

      serializer = AnimalSerializer(animal, data = request.data, partial = True)
      serializer.is_valid(raise_exception = True)
      try:
         serializer.save()
      except KeyError as error:
         return Response(*error.args)
   

      return Response(serializer.data , status.HTTP_200_OK)


   def delete(self, request, animal_id: int):
      try:
            animal = Animal.objects.get(id=animal_id)
      except Animal.DoesNotExist:
            return Response({'details': 'Content not found'}, status.HTTP_404_NOT_FOUND)

      animal.delete()

      return Response({""}, status.HTTP_204_NO_CONTENT)
