from rest_framework.routers import SimpleRouter

from users import views

router = SimpleRouter(trailing_slash=False)
router.register(r'users', views.UserViewSetAPI)
urlpatterns = router.urls
