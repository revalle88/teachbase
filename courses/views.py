from rest_framework import serializers
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from courses.models import Course
from courses.tasks import import_courses_from_teachbase
from rest_framework.response import Response


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'teachbase_id', 'name', 'description', )


class CoursesListApi(APIView):
    def get(self, request, format=None):
        import_courses_from_teachbase()
        return Response(status=200)


class CourseViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
