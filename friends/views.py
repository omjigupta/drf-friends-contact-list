from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Friend
from .serializers import FriendSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def get_post_friends(request):
    # get all friends
    if request.method == 'GET':
        friends = Friend.objects.all()
        serializer = FriendSerializer(friends, many=True)
        return Response(serializer.data)
    # insert a new record for a Friend
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'age': int(request.data.get('age')),
            'email': request.data.get('email'),
            'contact_number': request.data.get('contact_number'),
            'address': request.data.get('address')
        }
        serializer = FriendSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
