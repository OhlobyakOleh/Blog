from django.urls import path
from .views import BlogListView

urlpattern = [path('', BlogListView.as_view(), name='home'),]