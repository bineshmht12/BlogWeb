
from django.contrib import admin
from django.urls import path,include

from blog.views import BlogListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    path('',include('blog.urls')),
    path('', BlogListView.as_view(),name='home'),
    
]
