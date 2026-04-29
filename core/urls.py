from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from shop.views import (
    login_view, 
    logout_view, 
    register_view, 
    product_list, 
    product_detail
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'), 
    path('login/', login_view, name='login'),      
    path('logout/', logout_view, name='logout'), 
    path('register/', register_view, name='register'), 
    path('product/<int:pk>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)