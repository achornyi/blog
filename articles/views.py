from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import AuthorPermissions
# from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .service import TagsFilter
from .models import Article
from .serializers import ArticleSerializer, ArticleCreateSerializer, ArticleDetailsSerializer


class ArticleListView(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = (AuthorPermissions, permissions.IsAuthenticatedOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TagsFilter

    def get(self, request, format=None):
        snippets = Article.objects.all()
        serializer = ArticleSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailsView(generics.RetrieveUpdateAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = (AuthorPermissions, permissions.IsAuthenticatedOrReadOnly)
    queryset = Article.objects.all()
    serializer_class = ArticleDetailsSerializer
