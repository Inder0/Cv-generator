from django.urls import path
from .views import CreateProfileView,resume,ProfileDashboardView,delete_profile_redirect,download_resume

urlpatterns = [
    path('create/', CreateProfileView.as_view(),name="create_profile"),
    path('<int:pk>/',resume,name='resume'),
    path('',ProfileDashboardView.as_view(),name='home'),
    path('delete/<int:pk>/',delete_profile_redirect,name='delete_profile'),
    path('download/<int:pk>/',download_resume,name='download_resume')
]