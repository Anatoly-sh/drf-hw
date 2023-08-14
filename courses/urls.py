from rest_framework import routers

from courses.views import CourseViewSet

router = routers.SimpleRouter()
router.register('', CourseViewSet)


urlpatterns = router.urls
