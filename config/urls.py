from django.contrib import admin
from django.urls import path
from django.conf import settings
from django. conf.urls.static import static 
import page.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.views.home,name='home'),
    path('detail/<int:post_id>', page.views.detail, name='detail'),
    path('new/', page.views.new, name='new'),
] + static('/media/', document_root=settings.MEDIA_ROOT)