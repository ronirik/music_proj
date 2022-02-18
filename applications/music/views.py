from rest_framework import generics


from applications.music.serializers import MusicSerializer

from applications.music.models import Music


class MusicListView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
