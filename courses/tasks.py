from celery import shared_task
from rest_framework import serializers
from courses.models import Course

import requests


class ImportCourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='teachbase_id', required=False)
    class Meta:
        model = Course
        fields = (
            'id', 'name', 'description', 'duration', 'bg_url', 'video_url',
        )


@shared_task
def import_courses_from_teachbase():
    body = {
        'client_id': '8bdf8070ca5eb1ee7565aa4722e9772a60612310f62f0a04ba4774e7527c836b',
        'client_secret': 'c2c76197cc8de37d0d04a9cc4127ef7bb5c0961d4f96eeec6fff403e30b304dd',
        'grant_type': 'client_credentials'
    }
    response = requests.post('https://go.teachbase.ru/oauth/token/', json=body)
    token = response.json().get('access_token')
    headers = {'Authorization': f'Bearer {token}'}
    url = 'https://go.teachbase.ru/endpoint/v1/courses'
    response = requests.get(url, headers=headers)
    print('Courses Response')
    data = response.json()
    print(data)
    serializer = ImportCourseSerializer(data=data, many=True)
    if serializer.is_valid():
        Course.objects.all().delete()
        serializer.save()

    return None
