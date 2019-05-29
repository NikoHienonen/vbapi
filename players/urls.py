from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from players import views

urlpatterns = [
  path('players/', views.PlayerList.as_view()),
  path('players/<int:id>', views.PlayerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)