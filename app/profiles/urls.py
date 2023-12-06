from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles import views


router = DefaultRouter()
router.register('profile', views.UserView)
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.CreateTokenView.as_view(), name='login'),
]
