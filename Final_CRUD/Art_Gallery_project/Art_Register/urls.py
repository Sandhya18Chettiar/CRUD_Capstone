from . import views
from django.urls import path

from Art_Register.views import IndexView, ButtonView

# urlpatterns = [
#     path('',views.index),
#     path('buttons',views.buttons),
# ]

urlpatterns = [
    path('',IndexView.as_view()),
    path('buttons', ButtonView.as_view()),
]