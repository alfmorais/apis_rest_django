# pacotes essenciais da V1 da API
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

# pacotes essenciais da V2 da API
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions
from .permissions import IsSuperUser


# Versão 1
# ----------------------------------------------------------------------------------------------------
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get("curso_pk"):
            return self.queryset.filter(curso_id=self.kwargs.get("curso_pk"))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get("curso_pk"):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get("curso_id"),
                                     pk=self.kwargs.get("avaliacao_pk"))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("avaliacao_pk"))


# Versão 2
# ----------------------------------------------------------------------------------------------------
class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser, permissions.DjangoModelPermissions, )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


''' 
comentado antigo código:
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
'''


class AvaliacaoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
# ----------------------------------------------------------------------------------------------------
