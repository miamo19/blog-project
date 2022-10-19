from django.urls import path
from . import  views

urlpatterns = [
    path("", views.post_list, name="home"),
    path("category/<slug:category>/", views.post_list, name='category'),
    path("<year>/<month>/<day>/<slug>/", views.post_detail, name="detail")
]