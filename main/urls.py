from django.urls import path
from .views import IndexView, ArticleNewView, article_detail, manager_dashboard, MarketologDashboard


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/new', ArticleNewView.as_view(), name='article_new'),
    path('article/<int:article_id>/detail', article_detail, name='article_detail'),
    path('manager/dashboard', manager_dashboard, name='manager_dashboard'),
    path('marketolog/dashboard', MarketologDashboard.as_view() , name='marketolog_dashboard'),
]
