from django.urls import path
from .views import NewsListView, NewsDetailView, SearchView, SearchResultView, ArticleListView
from .views import NewsCreateView, NewsUpdateView, NewsDeleteView, LoginView, ArticleDetailView

app_name = 'news'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/search/', SearchView.as_view(), name='search'),
    path('news/search/results/', SearchResultView.as_view(), name='search_results'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]