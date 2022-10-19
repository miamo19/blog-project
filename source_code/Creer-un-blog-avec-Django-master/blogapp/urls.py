from django.urls import path
from blogapp.views import List, detailView

urlpatterns = [
    path('', List.as_view(), name="home"),
    path('detail/<slug:slug>', detailView, name='detailView'),
]