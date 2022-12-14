from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views

urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('movies/<int:movie_pk>/get-reviews/', views.movie_reviews),
    path('get-similar/', views.get_similar_user),
    # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # optional UI
    # api별로 필요한거
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]