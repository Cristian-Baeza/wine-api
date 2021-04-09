# DJANGO REST METHOD
from django.urls import path, include
from .views import WineViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', WineViewSet, basename='wine')
urlpatterns = router.urls


#MANUAL WAY 
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.wine_list, name='wine_list'),
#     path('new', views.new_wine, name='new_wine'),
#     path('<int:wine_id>', views.wine_detail, name='wine_detail'),
#     path('<int:wine_id>/edit', views.edit_wine, name='edit_wine'),
#     path('<int:wine_id>/delete', views.delete_wine, name='delete_wine'),
# ]