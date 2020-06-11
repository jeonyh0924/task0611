from django.urls import path
from rest_framework.routers import SimpleRouter

from users import views
from users.views import AuthTokenAPIView

router = SimpleRouter()
router.register('users', views.UserViewSetAPI)
urlpatterns = [
    path('token/', AuthTokenAPIView.as_view()),
]
urlpatterns += router.urls
