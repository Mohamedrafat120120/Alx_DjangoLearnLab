from rest_framework import generics,viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class BookList(generics.ListAPIView):
    data=Book.objects.all()
    
    serializer=BookSerializer(data,many=True)
    
    




class BookViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer   


    