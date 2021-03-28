from django.urls import path
from .views import (
    PortaListView,
    PortaDetailView,
    PortaCreateView,
    PortaUpdateView,
    PortaDeleteView,
    PortaGeraDetailView,
)
from . import views


urlpatterns = [
    # path('phone-one/new/', PostCreateView.as_view(), name='post-create'),
    # path('phone-many/new/', PostCreateView.as_view(), name='post-create'),
    # path('video-conference/new/', PostCreateView.as_view(), name='post-create'),
    path('all/', PortaListView.as_view(), name='porta-home'),
    path('all/old/<int:pk>/', PortaDetailView.as_view(), name='porta-detail'),
    path('all/new/', PortaCreateView.as_view(), name='porta-create'),
    path('all/<int:pk>/update/', PortaUpdateView.as_view(), name='porta-update'),
    path('all/<int:pk>/delete/', PortaDeleteView.as_view(), name='porta-delete'),
    path('all/<int:pk>/', PortaGeraDetailView.as_view(), name='porta-gera'),
    # path('about/', views.about, name='blog-about'),
]