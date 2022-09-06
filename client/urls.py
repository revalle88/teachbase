from client.views import CoursesListApi, CoursesDetailApi, UsersCreateApi, SessionsListApi, SessionUserRegisterApi
from rest_framework.routers import SimpleRouter
from django.urls import path, include

# router = SimpleRouter()
# router.register(r'courses', CoursesListApi.as_view(), basename='tb_courses')

urlpatterns = [
    path('courses/', CoursesListApi.as_view(), name='tb_courses_list'),
    path('courses/<int:teachbase_id>', CoursesDetailApi.as_view(), name='tb_courses_detail'),
    path('courses/<int:teachbase_id>/sessions', SessionsListApi.as_view(), name='tb_course_sessions'),
    path('course_sessions/<int:session_id>/register', SessionUserRegisterApi.as_view(), name='tb_course_session_register'),
    path('users/', UsersCreateApi.as_view(), name='tb_user_create'),
]
