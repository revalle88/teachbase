import requests
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class TeachBaseCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TeachBaseCourseDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TeachBaseUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    phone = serializers.CharField()
    role_id = serializers.IntegerField()


class TeachBaseSessionUserRegisterSerializer(serializers.Serializer):
    email = serializers.CharField()
    phone = serializers.CharField()
    user_id = serializers.IntegerField()


class TeachBaseCourseSessionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    participants = TeachBaseUserSerializer(many=True, required=False)


class CoursesListApi(APIView):
    def get(self, request, format=None):
        url = 'https://go.teachbase.ru/endpoint/v1/courses'
        print(request.tb_token)
        headers = {'Authorization': f'Bearer {request.tb_token}'}
        url = 'https://go.teachbase.ru/endpoint/v1/courses'
        response = requests.get(url, headers=headers)
        print('Courses Response')
        data = response.json()
        print(data)
        serializer = TeachBaseCourseSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)


class CoursesDetailApi(APIView):
    def get(self, request, teachbase_id):
        headers = {'Authorization': f'Bearer {request.tb_token}'}
        url = f'https://go.teachbase.ru/endpoint/v1/courses/{teachbase_id}'
        response = requests.get(url, headers=headers)
        print('Courses Response')
        data = response.json()
        print(data)
        serializer = TeachBaseCourseDetailSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.data, status=200)


class UsersCreateApi(APIView):
    def post(self, request):
        headers = {'Authorization': f'Bearer {request.tb_token}'}
        url = f'https://go.teachbase.ru/endpoint/v1/users/create'
        users = request.data.get('users')

        serializer = TeachBaseUserSerializer(data=users, many=True)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            print(data)
            print(users)
            response = requests.post(url, json={"users": users}, headers=headers)
            print('Yser Create  Response')
            response_data = response.json()
            print(response_data)
            return Response(response_data, status=200)


class SessionsListApi(APIView):
    def get(self, request, teachbase_id):
        url = f'https://go.teachbase.ru/endpoint/v1/courses/{teachbase_id}/course_sessions'
        print(request.tb_token)
        headers = {'Authorization': f'Bearer {request.tb_token}'}
        response = requests.get(url, headers=headers)
        print('Courses Response')
        data = response.json()
        print(data)
        serializer = TeachBaseCourseSessionSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)


class SessionUserRegisterApi(APIView):
    def post(self, request, session_id):
        url = f'https://go.teachbase.ru/endpoint/v1/course_sessions/{session_id}/register'
        headers = {'Authorization': f'Bearer {request.tb_token}'}
        user = request.data
        serializer = TeachBaseSessionUserRegisterSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            response = requests.post(url, json=user, headers=headers)
            return Response(response.json(), status=200)
