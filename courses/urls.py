from courses.views import CourseViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'api/courses', CourseViewSet, basename='courses')

urlpatterns = router.urls
