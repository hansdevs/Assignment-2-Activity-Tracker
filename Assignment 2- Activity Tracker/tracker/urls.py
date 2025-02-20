from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_activity/', views.new_activity, name='new_activity'),
    path('activity/<int:activity_id>/', views.activity_detail, name='activity_detail'),
    path('activity/<int:activity_id>/new_timelog/', views.new_timelog, name='new_timelog'),
]
