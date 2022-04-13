from django.urls import path
from Api import views

urlpatterns = [
    # path("", views.apiOverview),
    # path("buildings/", views.buildingList),
    # path("building/<int:id>/", views.buildingDetail),
    # path("building-create/", views.buildingCreate),
    # path("building-update/<int:id>", views.buildingUpdate),
    # path("building-delete/<int:id>", views.buildingDelete)
    path("", views.apiOverview), 
    path("buildings/", views.BuildingList.as_view()),
    path("buildings/<int:pk>/", views.BuildingDetails.as_view()),
    path("blocks/", views.BlockList.as_view()),
    path("blocks/<int:pk>/", views.BlockDetails.as_view())
]
