from django.urls import path
from Api import views

urlpatterns = [
    path("", views.apiOverview), 
    path("buildings/", views.BuildingList.as_view()),
    path("buildings/<int:pk>/", views.BuildingDetails.as_view()),
    path("buildings/<int:pk>/update-partial/", views.buildingUpdatePartial),
    path("blocks/", views.BlockList.as_view()),
    path("blocks/<int:pk>/", views.BlockDetails.as_view()),
]
