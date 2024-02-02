from django.urls import path
from .views import counter_view, create_view, list_view 

app_name = 'stimulus-basic'

urlpatterns = [
    path('counter/', counter_view, name='counter'),
    # path('turbo_frame_load/', turbo_frame_load_view, name='turbo_frame_load'),
    path('list/', list_view, name='task-list'),                   # new
    path('create/', create_view, name='task-create'), 
]