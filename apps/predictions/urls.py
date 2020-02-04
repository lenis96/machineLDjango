from rest_framework.urls import url
from apps.predictions.views import *


urlpatterns = [
    # url(r'^<int:pk>/$', PredictionAPIView.as_view()),
    url(r'^(?P<prediction>\w+)/$', PredictionAPIView.as_view()),
]
