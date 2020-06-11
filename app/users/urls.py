from django.urls import path
from rest_framework.routers import SimpleRouter

from rest_framework.authtoken import views

from users.views import AuthTokenAPIView, UserViewSetAPI

router = SimpleRouter()
router.register('users', UserViewSetAPI)
urlpatterns = [
    path('token/', AuthTokenAPIView.as_view()),
    path('api-token-auth/', views.obtain_auth_token)
]
urlpatterns += router.urls
