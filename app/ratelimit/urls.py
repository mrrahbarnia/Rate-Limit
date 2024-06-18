from django.urls import path

from . import apis

urlpatterns = [
    path('', apis.SampleApi.as_view(), name='sample'),
    path('login/', apis.FakeLoginApi.as_view(), name='login')
]