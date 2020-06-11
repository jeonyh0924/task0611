from rest_framework.routers import SimpleRouter

from cards import views

router = SimpleRouter()
router.register('card', views.CardModelViewSetAPI)
urlpatterns = router.urls
