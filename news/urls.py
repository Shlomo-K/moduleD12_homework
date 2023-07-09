from django.urls import path
from .views import NewsList, PostDetail, SearchNews, PostCreateView, PostDeleteView, PostUpdateView, subscription 
from django.views.decorators.cache import cache_page
 
urlpatterns = [
   
    
    path('', cache_page(60*1)(NewsList.as_view())),
    path('<int:pk>/', ), 
    path('search/', SearchNews.as_view()),
    path('add/', PostCreateView.as_view(), name='add_post'), 
    path('<int:pk>/', cache_page(60*5)(PostDetail.as_view()), name='detail_post'),
    path('subscription/', subscription, name='subscription'),
    path('add/<int:pk>', PostUpdateView.as_view(), name='edit_post'), 
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'), 
 

]