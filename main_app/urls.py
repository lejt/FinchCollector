from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('finches/',views.finches_index, name='finches_index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail'),

    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),

    path('finches/<int:finch_id>/assoc_birdacc/<int:birdacc_id>/', views.assoc_birdacc, name='assoc_birdacc'),

    path('birdacc/', views.BirdAccList.as_view(), name='birdacc_index'),
    path('birdacc/create/', views.BirdAccCreate.as_view(), name='birdacc_create'),
    path('birdacc/<int:pk>/', views.BirdAccDetail.as_view(), name='birdacc_detail'),
    path('birdacc/<int:pk>/update', views.BirdAccUpdate.as_view(), name='birdacc_update'),
    path('birdacc/<int:pk>/delete', views.BirdAccDelete.as_view(), name='birdacc_delete'),
]