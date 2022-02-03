from django.urls import path
from django.http import HttpRequest,HttpResponse
from about import views

app_name = 'about'
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:usr_name>/", views.user_info, name='user_info'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]