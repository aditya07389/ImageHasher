from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ImageRecord
from .serializers import ImageRecordSerializer
from .utils import calculate_md5, calculate_phash
import requests
from urllib.parse import urlparse
from rest_framework import generics 

class ImageRecordListCreate(generics.ListCreateAPIView):
    queryset = ImageRecord.objects.all()
    serializer_class = ImageRecordSerializer

    def create(self, request, *args, **kwargs):
        image_url = request.data.get('image_url')

       
        parsed_url = urlparse(image_url)
        if not parsed_url.scheme:
            return Response({"error": "Invalid URL. Please provide a valid URL with a scheme (e.g., http:// or https://)"}, 
                             status=status.HTTP_400_BAD_REQUEST)
        
        try:
           
            response = requests.get(image_url)
            response.raise_for_status()  # Will raise an HTTPError for bad status codes 
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Failed to download image. Error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        image_content = response.content
        md5_hash = calculate_md5(image_content)
        phash = calculate_phash(image_content)

        
        image_record = ImageRecord.objects.create(
            image_url=image_url,
            md5_hash=md5_hash,
            phash=phash
        )
        
        return Response({
            "id": image_record.id,
            "image_url": image_url,
            "md5_hash": md5_hash,
            "phash": phash
        }, status=status.HTTP_201_CREATED)


class ImageRecordRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageRecord.objects.all()
    serializer_class = ImageRecordSerializer
