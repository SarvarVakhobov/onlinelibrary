from django.urls import include, path
from .views import RegisterView, UserDetailView, CreateListUserView, ChangePasswordView
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'userlist', UserListView.as_view({'get': 'list'}), basename='userlist')
# router.register(r'userdetails', UserListView.as_view({'get': 'retrieve'}), basename='userdetails')

urlpatterns = [
    
    path('userlist/', CreateListUserView.as_view(), name='userlist'),
    path('userdetails/<int:pk>/', UserDetailView.as_view({'get': 'retrieve'}), name='userdetails'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password')
]



